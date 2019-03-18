import re


def GetUsername(email_address):
    match = re.match(r'([^@]+)@example\.com', email_address)
    if match is None:
        return None
    return match.group(1)  # <-- Here, match can't be None
