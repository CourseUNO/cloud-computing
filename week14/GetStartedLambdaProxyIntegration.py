import json

keys = [
    'multiValueQueryStringParameters',
    'multiValueHeaders',
    'queryStringParameters',
    'headers',
]


def lambda_handler(event, context):
    print(event)

    greeter = ''

    for keyword in keys:
        try:
            if ((event[keyword]) and
                    (event[keyword]['greeter']) and
                    (event[keyword]['greeter'] is not None)):
                if 'multi' in keyword:
                    greeter += f' from {", ".join(event[keyword]["greeter"])} [{keyword}];\n'
                else:
                    greeter += f' from {event[keyword]["greeter"]} [{keyword}];\n'
        except KeyError:
            print(f'No greeter from {keyword}')

    if (event['body']) and (event['body'] is not None):
        body = json.loads(event['body'])
        try:
            if (body['greeter']) and (body['greeter'] is not None):
                greeter = body['greeter'] + ' from body'
        except KeyError:
            print('No greeter from body')

    res = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        },
        "body": "Hello world!\n " + greeter + "\n" * 5 + json.dumps(event, indent=2)
    }

    return res
