import hashlib
import sys

PY2 = sys.version_info[0] == 2
if PY2:
    unicode_type = unicode
else:
    unicode_type = str


def force_bytes(s, encoding="utf-8", errors="strict"):
    if isinstance(s, unicode_type):
        s = s.encode(encoding, errors)
    return s


str1 = "abcd"
hashed = hashlib.md5(force_bytes(str1)).hexdigest()
print(hashed)
