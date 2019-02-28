import os

if 'PYTHONDONTWRITEBYTECODE' in os.environ:
    print(os.environ.get('PYTHONDONTWRITEBYTECODE', 'BAD-VALUE'))
else:
    print('not in system variables: PYTHONDONTWRITEBYTECODE')
