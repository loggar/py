n_odds = 0

for i in range(1, 14, 2):
    # Check for the value of i in each iteration
    breakpoint()
    # Bad condition
    if i % 2 == 0:
        n_odds += 1

print("n_odds ", n_odds)

# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(7)<module>()
# -> if i % 2 == 0:
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(5)<module>()
# -> breakpoint()
# (Pdb) i
# 3
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(7)<module>()
# -> if i % 2 == 0:
# (Pdb) i
# 5
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(5)<module>()
# -> breakpoint()
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(7)<module>()
# -> if i % 2 == 0:
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(5)<module>()
# -> breakpoint()
# (Pdb) continue
# > c:\users\webnl\documents\_workspace\loggar-py\py-dev\debug\debugger.call.py(7)<module>()
# -> if i % 2 == 0:
# (Pdb) continue
# n_odds 0
