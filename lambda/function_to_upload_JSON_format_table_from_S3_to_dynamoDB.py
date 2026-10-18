import json
import boto3

s3_client = boto3.client('s3')
dynamodb_client = boto3.resource('dynamodb')


# function to load JSON data from S3 bucket and push to DynamoDB table
def lambda_handler(event, context):
    # retrieve JSON data from S3 bucket
    bucket_name = "lambda-tables"
    file_name = "json/employees.json"
    s3_response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    employees_data = json.loads(s3_response['Body'].read())

    # dynamoDB table details
    table_dynamodb = dynamodb_client.Table("employees_json_table")

    with table_dynamodb.batch_writer() as batch:
        for item in employees_data:
            batch.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
