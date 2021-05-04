from functools import reduce

c = map(lambda x: x+x, filter(lambda x: (x >= 3), (1, 2, 3, 4)))
print(list(c))

c = filter(lambda x: (x >= 3), map(
    lambda x: x+x, (1, 2, 3, 4)))  # lambda x: (x>=3)
print(list(c))

d = reduce(lambda x, y: x+y, map(lambda x: x+x,
                                 filter(lambda x: (x >= 3), (1, 2, 3, 4))))
print(d)
