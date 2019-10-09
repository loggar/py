def func(x):
    if x >= 3:
        return x


y = filter(func, (1, 2, 3, 4))
print(y)
print(list(y))
