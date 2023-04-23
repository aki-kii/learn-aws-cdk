import json

def lambda_handler(event, context):
    print(f'request: {json.dumps(event)}')
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/plain" },
        "body": f"Good Afternoon, CDK! You've hit {event['path']}\n"
    }