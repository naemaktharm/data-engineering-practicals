import json
import boto3
import datetime

sqs_client = boto3.client("sqs")

def lambda_handler(event, context):

sqs_client = boto3.client("sqs", region_name="us-east-1")

def lambda_handler(event, context):
    queue_response = sqs_client.get_queue_url(
        QueueName="sqsQueueFromLambda"
    )
    queue_url = queue_response["QueueUrl"]

    current_time = datetime.datetime.now(
        datetime.timezone.utc
    ).isoformat()

    sqs_response = sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=f"Hello World from Lambda at {current_time}"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Message sent successfully",
            "message_id": sqs_response["MessageId"]
        })
    }
