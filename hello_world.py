import json


def hello(event, context):
    print('hello')
    body = {
        "message": "Greetings from the serverless API :) ",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
