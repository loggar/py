
add_func = lambda z: z ** 2
is_odd = lambda z: z%2 == 1
multiply = lambda x,y: x*y

aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(add_func, aList)))
print([x ** 2 for x in aList])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(filter(is_odd, aList)))
print([x for x in aList if x % 2 == 1])
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9]
