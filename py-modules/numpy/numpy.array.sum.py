import numpy as np

arr2d = np.arange(25).reshape(5, 5)
print(arr2d)

"""
OUTPUT: [
[ 0  1  2  3  4]
[ 5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]
]
"""

print(arr2d.sum())
# OUTPUT: 300

print(arr2d.sum(axis=0))  # sum of columns
# OUTPUT: [50 55 60 65 70]

print(arr2d.sum(axis=1))  # sum of rows
# OUTPUT: [ 10  35  60  85 110]
