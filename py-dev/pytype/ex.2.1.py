import re
from typing import Match, Optional


def GetEmailMatch(email) -> Optional[Match]:
    return re.match(r'([^@]+)@example\.com', email)
