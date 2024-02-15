from http.cookies import SimpleCookie
import os

fileName = "input.cookie.sample.txt"

try:
    # Resolve the file path
    file_path = os.path.join(os.getcwd(), fileName)

    # Read the file
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    cookie_string = data

except Exception as err:
    print(f"An error occurred: {err}")
    exit(1)

# Create a SimpleCookie object
cookie = SimpleCookie()
cookie.load(cookie_string)

# Extracting the cookie's name-value pair and attributes
for key, morsel in cookie.items():
    print(f"Key: {key}")
    print(f"Value: {morsel.value}")
    for attr in morsel.keys():
        print(f"{attr.capitalize()}: {morsel[attr]}")
