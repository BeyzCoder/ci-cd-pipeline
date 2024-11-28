import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name="us-east-1"
)

# Initialize a session using Amazon DynamoDB
dynamodb = session.resource('dynamodb', region_name='us-east-1')  # e.g., 'us-west-2'

# Specify the table
table = dynamodb.Table('financial-statements')


def dynamo_to_dict(item) -> dict:
    return {k: {year: float(dec) for year, dec in v.items()} for k, v in item.items()}


def put_item(statement: dict, symbol: str) -> dict:
    """Insert an item into DynamoDB."""
    try:
        print(symbol)
        item = {
            "symbol": symbol,
            "statement": statement
        }
        response = table.put_item(Item=item)
        return {"status": "PutItem succeeded", "response": response}
    except (BotoCoreError, ClientError) as e:
        return {"status": "FAILED", "error": str(e)}


def get_item(key: dict) -> dict:
    """Retrieve an item from DynamoDB."""
    try:
        response = table.get_item(Key=key)
        item = response.get('Item')

        if not item:
            return {"status": "Item not found"}

        # Remove the partition key from the item
        item.pop('symbol', None)

        item = dynamo_to_dict(item['statement'])
        return {"status": "GetItem succeeded", "item": item}
    except (BotoCoreError, ClientError) as e:
        return {"status": "FAILED", "error": str(e)}
