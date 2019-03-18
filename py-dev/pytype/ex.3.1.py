import re
from typing import Match
from typing import Optional


def GetEmailMatch(email) -> Optional[Match[str]]:
    return re.match(r'([^@]+)@example\.com', email)


def GetUsername(email_address) -> Optional[str]:
    match = GetEmailMatch(email_address)
    if match is None:
        return None
    return match.group(1)
