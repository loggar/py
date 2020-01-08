numList = [0, 1, 2]
engList = ['zero', 'one', 'two']
espList = ['cero', 'uno', 'dos']
print(list(zip(numList, engList, espList)))
# [(0, 'zero', 'cero'), (1, 'one', 'uno'), (2, 'two', 'dos')]

for num, eng, esp in zip(numList, engList, espList):
    print(f'{num} is {eng} in English and {esp} in Spanish.')
# 0 is zero in English and cero in Spanish.
# 1 is one in English and uno in Spanish.
# 2 is two in English and dos in Spanish.

eng = list(zip(engList, espList, numList))
eng.sort()  # sort by engList
a, b, c = zip(*eng)

print(a)
print(b)
print(c)
# ('one', 'two', 'zero')
# ('uno', 'dos', 'cero')
# (1, 2, 0)
