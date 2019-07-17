def z():
    n = 1
    yield n
    n = n+3
    yield n


p = z()
print(next(p))
print(next(p))
print(next(p))
