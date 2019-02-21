import os

process_env = 'development'

if 'NODE_ENV' in os.environ:
    process_env = os.environ.get('NODE_ENV', 'development')
else:
    print('not in system variables: NODE_ENV')

print('process_env: %s' % process_env)
