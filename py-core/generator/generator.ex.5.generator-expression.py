"""
You can also use expressions along with the for loop to produce iterators.
This usually makes the generation iterables much easy.
Generator expression resemble list comprehensions and like lambda functions, generator expressions create anonymous generator functions.
"""
a = range(6)
print("List Comprehension", end=':')
b = [x+2 for x in a]
print(b)
print("Generator expression", end=':n')
c = (x+2 for x in a)
print(c)
for y in c:
    print(y)
