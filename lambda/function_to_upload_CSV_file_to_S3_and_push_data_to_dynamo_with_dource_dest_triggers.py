import json
import csv
import io
import boto3
from urllib.parse import unquote_plus

s3_client = boto3.client("s3")
dynamodb_resource = boto3.resource("dynamodb")


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Get files from an actual S3 event
    if "Records" in event:
        files = [
            (
                record["s3"]["bucket"]["name"],
                unquote_plus(record["s3"]["object"]["key"])
            )
            for record in event["Records"]
        ]

    # Handle a custom test event
    else:
        if event.get("status", "").upper() != "SUCCESS":
            raise RuntimeError("Data processing failed")

        files = [
            (
                "lamda-with-source-triggers-csv",
                event["filename"]
            )
        ]

    employees_table_dynamodb = dynamodb_resource.Table(
        "employees_table"
    )

    inserted_count = 0

    for bucket_name, file_name in files:
        s3_response = s3_client.get_object(
            Bucket=bucket_name,
            Key=file_name
        )

        body = s3_response["Body"]
        try:
            csv_content = body.read().decode("utf-8-sig")
        finally:
            body.close()

        for employee in csv.DictReader(io.StringIO(csv_content)):
            # If employee_id is a Number key, uncomment:
            # employee["employee_id"] = int(employee["employee_id"])

            employees_table_dynamodb.put_item(Item=dict(employee))
            inserted_count += 1

    print(f"Successfully inserted {inserted_count} employee records")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Data processing completed successfully",
            "records_inserted": inserted_count
        })
    }