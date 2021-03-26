import numpy as np

myarr = np.arange(0, 11)
print(myarr)
# OUTPUT:[ 0  1  2  3  4  5  6  7  8  9 10]

sliced = myarr[0:5]
print(sliced)
# OUTPUT: [0 1 2 3 4]

sliced[:] = 99
print(sliced)
# OUTPUT: [99 99 99 99 99]

print(myarr)
# OUTPUT:[99 99 99 99 99  5  6  7  8  9 10]

# To make an independent section of an array, use the copy() function.

sliced = myarr.copy()[0:5]
