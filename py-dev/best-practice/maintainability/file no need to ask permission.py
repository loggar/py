"""
import os

# violates EAFP coding style
if os.path.exists("file.txt"):
    os.unlink("file.txt")
"""

import os

try:
    os.unlink("file.txt")
# raised when file does not exist
except OSError:
    pass
