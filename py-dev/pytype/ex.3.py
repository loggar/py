# Merging back inferred type information

import re


def GetEmailMatch(email):
    return re.match(r'([^@]+)@example\.com', email)


def GetUsername(email_address):
    match = GetEmailMatch(email_address)
    if match is None:
        return None
    return match.group(1)

# pytype ex.3.py
# merge-pyi -i ex.3.py _pytype_output/ex.3.pyi