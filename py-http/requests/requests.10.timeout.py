from requests.exceptions import Timeout
import requests

requests.get('https://api.github.com', timeout=1)

requests.get('https://api.github.com', timeout=3.05)

requests.get('https://api.github.com', timeout=(2, 5))


try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')
