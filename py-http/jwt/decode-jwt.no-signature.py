import json
import jwt
import os

tokenFilePath = "token.txt"

# Resolve the file path
tokenFile = os.path.join(os.getcwd(), tokenFilePath)

# Read token from the file
with open(tokenFile, "r") as tFile:
    jwt_token = tFile.read().strip()

# Attempt to decode the JWT without verification
try:
    decoded = jwt.decode(jwt_token, options={"verify_signature": False})
    print(json.dumps(decoded, indent=4))
except jwt.InvalidTokenError as e:
    print("Invalid token:", e)
