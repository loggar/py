with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
