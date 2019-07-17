a = range(10)
b = (x for x in a)
print(b)
for y in b:
    print(y)


c = range(2, 10, 2)
d = (x for x in c)
print(d)
for y in d:
    print(y)
