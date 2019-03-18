# Type inference and checking

import re


def GetUsername(email_address):
    match = re.match(r'([^@]+)@example\.com', email_address)
    return match.group(1)
