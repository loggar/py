import os

process_env = 'production'

os.environ["PY_ENV"] = process_env

print(os.environ.get('PY_ENV', 'development'))
