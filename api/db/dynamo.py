import boto3
from botocore.exceptions import BotoCoreError, ClientError

# Initialize a session using Amazon DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='your-region')  # e.g., 'us-west-2'

# Specify the table
table = dynamodb.Table('YourTableName')


def put_item(item: dict) -> dict:
    """Insert an item into DynamoDB."""
    try:
        response = table.put_item(Item=item)
        return {"status": "PutItem succeeded", "response": response}
    except (BotoCoreError, ClientError) as e:
        return {"status": "FAILED", "error": str(e)}


def get_item(key: dict) -> dict:
    """Retrieve an item from DynamoDB."""
    try:
        response = table.get_item(Key=key)
        item = response.get('Item')
        if item:
            return {"status": "GetItem succeeded", "item": item}
        else:
            return {"status": "Item not found"}
    except (BotoCoreError, ClientError) as e:
        return {"status": "FAILED", "error": str(e)}
