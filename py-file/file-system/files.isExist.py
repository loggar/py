# Brute force with a try-except block (Python 3+)
try:
import os
from pathlib import Path
with open('/path/to/file', 'r') as fh:
        pass
except FileNotFoundError:
    pass

# Leverage the OS package (possible race condition)
exists = os.path.isfile('/path/to/file')

# Wrap the path in an object for enhanced functionality
config = Path('/path/to/file')
if config.is_file():
    pass
