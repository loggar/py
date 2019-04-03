alpha = 7

if alpha > 7:
    beta = 999
elif alpha == 7:
    beta = 99
else:
    beta = 0
print(beta)

# shortcut
beta = 999 if alpha > 7 else 99 if alpha == 7 else 0
print(beta)
