import json
import boto3
import awswrangler as wr

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    try:
        bucket = "lambda-parquet-26-oct"
        input_key = "car_models_test.parquet"
        output_key = "output/car_models_categories.json"

        df = wr.s3.read_parquet(
            path=f"s3://{bucket}/{input_key}"
        )

        result = []

        for _, row in df.iterrows():
            price = int(row["price"])

            if price < 135000:
                category = "Class A Car"
            elif price < 170000:
                category = "Class B Car"
            elif price < 220000:
                category = "Class C Car"
            else:
                category = "Class D Car"

            result.append({
                "car_model": row["model"],
                "price": price,
                "category": category
            })

        # Save JSON to S3; an empty DataFrame produces []
        s3_client.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=json.dumps(result, indent=2).encode("utf-8"),
            ContentType="application/json"
        )

        output_path = f"s3://{bucket}/{output_key}"
        print(f"Saved {len(result)} records to {output_path}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "JSON file saved successfully",
                "records": len(result),
                "output_path": output_path
            })
        }

    except Exception as e:
        print(f"Error processing Parquet file: {e}")

        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }