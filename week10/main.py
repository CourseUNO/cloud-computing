import json

import boto3
import sqlalchemy

s3 = boto3.client('s3')

print(sqlalchemy.__version__)

print('from cli update!')

print('S3 upload event trigger added for function demo!')

print('Deployed from Windows')

def main(event, context):
    # TODO implement
    print('from local main.main zip package deployment ')
    print(event)
    print(context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! Yes it is from Lambda! Deployed from Windows!')
    }
