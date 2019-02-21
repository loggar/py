import configparser

config = configparser.ConfigParser()
config.read('config.ex.ini')

topsecret = config['topsecret.server.com']

print(int(topsecret['Port']))
print(float(topsecret['CompressionLevel']))
print(topsecret.getboolean('ForwardX11'))
print(config['bitbucket.org'].getboolean('ForwardX11'))
print(config.getboolean('bitbucket.org', 'Compression'))
