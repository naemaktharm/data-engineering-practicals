import json
import boto3
import awswrangler as wr
import pandas as pd
from datetime import datetime

# initiate s3 client
s3_client = boto3.client("s3")

# initiate dynamodb resource
dynamodb_resource = boto3.resource("dynamodb")

# initiate dynamodb table resource
table = dynamodb_resource.Table("dq-check-status")

# initiate sqs client
sqs_client = boto3.client("sqs")

# define sqs queue url
sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/026343683315/sqsSuccessQueueForLambda"


# function to read S3 bucket parquet file and insert data quality check to dynamodb and notify using SQS
def lambda_handler(event, context):
    try:
        bucket = "lambda-parquet-dynamo-sqs"
        input_key = "car_models_prices_20_rows.parquet"
        output_key = "car_models_categories.json"
        output_bucket = "lambda-s3-output-store"

        df = wr.s3.read_parquet(path=f"s3://{bucket}/{input_key}")
        row_count = len(df)
        result = []

        for _, row in df.iterrows():
            price = int(row["price"])

            if price < 135000:
                category = "Economy"
            elif price < 170000:
                category = "Mid-Size"
            elif price < 220000:
                category = "Upper-Mid"
            else:
                category = "Luxury"

            result.append({
                "car_model": row["model"],
                "price": price,
                "category": category
            })

        s3_client.put_object(
            Bucket=output_bucket,
            Key=output_key,
            Body=json.dumps(result, indent=2).encode("utf-8"),
            ContentType="application/json"
        )
        output_path = f"s3://{output_bucket}/{output_key}"
        print(f"Saved  {len(result)} records to {output_path}.")

        # define the item to be stored in dynamodb
        item = {
            "object": input_key,
            "bucket_name": bucket,
            "status": "success",
            "timestamp": str(datetime.now()),
            "row_count": row_count
        }

        # store the values to the dynamodb table
        table.put_item(Item=item)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = "JSON file saved successfully, quality checks are added to dynamodb and sqs message triggered at " + current_time
        print("test message" + message)
        response = sqs_client.send_message(QueueUrl=sqs_queue_url, MessageBody=message)

        return {
            'statusCode': 200,
            'body': json.dumps({
                "message": "JSON file saved successfully, quality checks are added to dynamodb and sqs message triggered.",
                "records": len(result),
                "output_path": output_path,
                "sqs_message_id": response['MessageId']
            })
        }

    except Exception as e:
        print(f"Error processing Parquet file: {e}")

        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": str(e)
            })
        }

