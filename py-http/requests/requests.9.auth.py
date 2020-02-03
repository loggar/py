from getpass import getpass
import requests
from requests.auth import HTTPBasicAuth

requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)
