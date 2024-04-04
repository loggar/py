import jwt
import os

tokenFilePath = "token.txt"
keyFilePath = "jwt.public.key"

# Resolve the file path
tokenFile = os.path.join(os.getcwd(), tokenFilePath)
keyFile = os.path.join(os.getcwd(), keyFilePath)

# Read token from the file
with open(tokenFile, "r") as tFile:
    jwt_token = tFile.read().strip()

# Load the secret key from the JSON file
with open(keyFile, "r") as kFile:
    public_key = kFile.read()

# Decode the token
try:
    # Decode the JWT token
    decoded_jwt = jwt.decode(jwt_token, public_key, algorithms=["RS256"])
    print(decoded_jwt)
except jwt.ExpiredSignatureError:
    print("Signature expired. Please log in again.")
except jwt.InvalidTokenError:
    print("Invalid token. Please log in again.")
