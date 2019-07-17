a = 3


def myfunc(a):
    while a > 2 and a < 6:
        yield a
        a = a+1


b = myfunc(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
