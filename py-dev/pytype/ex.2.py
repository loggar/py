# Validation of type annotations

import re
from typing import Match


def GetEmailMatch(email) -> Match:
    return re.match(r'([^@]+)@example\.com', email)
