import requests

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
response.request.headers['Content-Type']

response.request.url

response.request.body
