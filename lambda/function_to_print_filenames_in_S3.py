import json
import boto3

s3_client = boto3.client('s3')


# Function to return the file names in the S3 bucket folder
def lambda_handler(event, context):
    bucket_name = "empty-bucket-lambda"

    # s3 bucket response
    s3_bucket_response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Iterating through the S3 bucket folder and printing the file names
    if 'Contents' in s3_bucket_response:
        for file in s3_bucket_response['Contents']:
            print(file['Key'])
    else:
        print("No files found in the S3 bucket.")


    print(s3_bucket_response)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
