import requests

requests.post('https://httpbin.org/post', data={'key': 'value'})

requests.post('https://httpbin.org/post', data=[('key', 'value')])

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = response.json()
print(json_response['data'])

print(json_response['headers']['Content-Type'])
