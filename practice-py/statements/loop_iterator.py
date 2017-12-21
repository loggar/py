import sys

list1 = [1, 2, 3, 4]
it = iter(list1)  # this builds an iterator object

for x in it:
    print(x, end=" ")


it2 = iter(list1)

while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()  # you have to import sys module for this
