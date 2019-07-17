def z():
    n = 1
    yield n
    n = n+3
    yield n


for x in z():
    print(x)
