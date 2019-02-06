import requests

response = requests.get('https://api.github.com/users/loggar')

# response contents
print(response.content)
print(response.text)

response.encoding = 'utf-8'  # Optional: requests infers this internally
print(response.text)

print(response.json())

# response headers
print(response.headers)
print(response.headers['Content-Type'])
print(response.headers['content-type'])
