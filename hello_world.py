import json


def hello(event, context):
    body = {
        "message": "Greetings from the serverless API :) ",
        "input": event
    }
    print('sssssssss')
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
