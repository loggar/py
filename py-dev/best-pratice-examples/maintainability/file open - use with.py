"""
f = open("file.txt", "r")
content = f.read()
1 / 0  # ZeroDivisionError
# never executes, possible memory issues or file corruption
f.close()
"""

with open("file.txt", "r") as f:
    content = f.read()
    # Python still executes f.close() even though an exception occurs
    1 / 0
