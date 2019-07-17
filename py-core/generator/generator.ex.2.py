a = 2


def myfunc(a):
    while a >= 0:
        yield a
        a -= 1


b = myfunc(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
