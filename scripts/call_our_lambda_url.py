import requests
from requests_auth_aws_sigv4 import AWSSigV4

FURL = '<replace-with-your-function-url>'

def call_api():
    aws_auth = AWSSigV4('lambda')
    r = requests.request('GET', FURL, auth=aws_auth)
    print(r.content)

if __name__ == '__main__':
    call_api()
