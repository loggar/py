import sys

# reference
mylist = range(0, 10000)
print(sys.getsizeof(mylist))

# real
myreallist = [x for x in range(0, 10000)]
print(sys.getsizeof(myreallist))
