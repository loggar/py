import hashlib
import six

s = "abcd"
hashed = hashlib.md5(six.ensure_binary(s)).hexdigest()

print(hashed)