import json
import boto3
import pandas as pd
from io import StringIO, BytesIO
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]
    json_file = os.environ["JSON_FILE"]

    # Download the JSON file from S3
    json_file_response = s3_client.get_object(Bucket=bucket_name, Key=json_file)

    # # Read the JSON file from the S3 response
    json_file_formatted = json_file_response['Body'].read().decode('utf-8')

    # # Read the JSON file into a Pandas DataFrame
    df_json = pd.read_json(StringIO(json_file_formatted), orient = "records")

    # json_object = json.loads(json_file_response['Body'].read())

    print("JSON:")
    print(df_json)

    return {
        'statusCode': 200,
        'body': json.dumps('JSON file processed successfully')
    }
