def newfunc(a):
    return a*a


x = map(newfunc, (1, 2, 3, 4))  # x is the map object
print(x)
print(set(x))


def newfunc2(a):
    return a*a


x = map(newfunc2, (1, 2, 3, 4))  # x is the map object
print(x)
print(list(x))


def func(a, b):
    return a + b


a = map(func, [2, 4, 5], [1, 2, 3])
print(a)
print(tuple(a))
