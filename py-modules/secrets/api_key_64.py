import secrets
import string


def generate_secure_key(length=64):
    # Define the characters to include in the key
    characters = string.ascii_letters + string.digits + "_"
    # Generate a secure random string of specified length
    secure_key = "".join(secrets.choice(characters) for i in range(length))
    return secure_key


# Generate a 64-character long key
key = generate_secure_key()
print(key)
