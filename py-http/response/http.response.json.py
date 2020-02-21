import requests

apod_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
apod_dict = requests.get(apod_url).json()

print(apod_dict['explanation'])
