import json


def hello(event, context):
    body = {
        "message": "Hello from my secure Lambda!",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
