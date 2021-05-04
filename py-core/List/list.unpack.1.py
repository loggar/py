
aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, c, d = aList[0:4]
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# a = 0, b = 1, c = 2, d = 3

a, *b, c, d = aList
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# a = 0, b = [1, 2, 3, 4, 5, 6, 7], c = 8, d = 9
