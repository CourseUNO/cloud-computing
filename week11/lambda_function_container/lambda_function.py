import json

import colored
from colored import Fore, Back, Style

print("This is from Lambda docker image deployment! an updated version is available")
print(colored.__version__)
print(f'{Fore.red}{Back.green}Colored is Awesome!!!{Style.reset}')
print('lambda function is running')

def handler(event, context):
    # TODO implement
    print(event)
    print(context)
    return {
        'statusCode': 200,
        'body': json.dumps('This is from Lambda docker image deployment! an updated version is available')
    }