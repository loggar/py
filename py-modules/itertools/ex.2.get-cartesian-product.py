import itertools

x, y, z = (2, 8), ['u', 'v', 'w'], {True, False}

lst = list(itertools.product(x, y, z))

print(lst)
