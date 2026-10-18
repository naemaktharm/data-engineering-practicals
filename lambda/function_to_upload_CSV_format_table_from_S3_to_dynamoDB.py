import json
import boto3

# defining boto3 clients
s3_client = boto3.client('s3')
dynamodb_client = boto3.resource('dynamodb')

# function to upload csv data from s3 to dynamodb
def lambda_handler(event, context):
    # s3 bucket details
    bucket_name = "lambda-tables"
    file_name = "csv/employees.csv"

    # reading csv file from s3
    s3_response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    csv_content = s3_response['Body'].read().decode('utf-8')

    employees_table_dynamodb = dynamodb_client.Table("employees_table_new")

    employees_list = csv_content.split("\n")
    csv_header = employees_list[0].split(",")

    # removing header row from list
    employees_list.pop(0)

    # iterate through the employees_list and update in dynamodb table
    for employee in employees_list:

        if len(employee) > 0:
            employee_details = employee.split(",")
            # print(csv_header[0])
            # print(employee_details[0])

            # updating the item in dynamodb table
            employees_table_dynamodb.put_item(Item = {
                csv_header[0] : employee_details[0],
                csv_header[1] : employee_details[1],
                csv_header[2] : employee_details[2],
                csv_header[3] : employee_details[3],
                csv_header[4] : employee_details[4],
                csv_header[5] : employee_details[5],
                }
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
