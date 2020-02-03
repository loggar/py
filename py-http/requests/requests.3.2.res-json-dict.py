import requests

apod_url = 'https://api.github.com/users/loggar'
apod_dict = requests.get(apod_url).json()

print(apod_dict['login'])
print(apod_dict['public_repos'])
