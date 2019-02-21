import configparser

config = configparser.ConfigParser()
config.read('config.ex.ini')

topsecret = config['topsecret.server.com']

print(topsecret.get('Port'))
print(topsecret.get('CompressionLevel'))
print(topsecret.get('Cipher'))
print(topsecret.get('Cipher', '3des-cbc'))
print(topsecret.get('CompressionLevel', '3'))

print(config.get('bitbucket.org', 'monster',
                 fallback='No such things as monsters'))

print('BatchMode' in topsecret)
print(topsecret.getboolean('BatchMode', fallback=True))

config['DEFAULT']['BatchMode'] = 'no'
print(topsecret.getboolean('BatchMode', fallback=True))
