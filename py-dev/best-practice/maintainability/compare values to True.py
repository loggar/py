"""
flag = True

# Not PEP 8's preferred pattern
if flag == True:
    print("This works, but is not the preferred PEP 8 pattern")
"""

flag = True

if flag:
    print("PEP 8 Style Guide prefers this pattern")

if flag is True:
    print("PEP 8 Style Guide abhors this pattern")
