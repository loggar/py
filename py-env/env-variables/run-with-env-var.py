import os

# export PY_ENV=production && python3 run-with-env-var.py (linux)
# $Env:PY_ENV = 'production'; python .\run-with-env-var.py (powershell)

py_env = 'development'
if 'PY_ENV' in os.environ:
    py_env = os.environ.get('PY_ENV', 'development')
if py_env != 'production':
    py_env = 'development'

print(py_env)
