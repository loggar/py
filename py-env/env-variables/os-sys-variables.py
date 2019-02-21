import os

if 'HOME' in os.environ:
    print(os.environ.get('HOME', 'BAD-VALUE'))
else:
    print('not in system variables: HOME')

if 'NODE_ENV' in os.environ:
    print(os.environ.get('NODE_ENV', 'BAD-VALUE'))
else:
    print('not in system variables: NODE_ENV')
