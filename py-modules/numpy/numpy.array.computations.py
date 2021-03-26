import numpy as np

new_arr = np.arange(1, 11)
print(new_arr)
# OUTPUT: [ 1  2  3  4  5  6  7  8  9 10]

# Addition
print(new_arr + 5)
# OUTPUT: [ 6  7  8  9 10 11 12 13 14 15]

# Subtraction
print(new_arr - 5)
# OUTPUT: [-4 -3 -2 -1  0  1  2  3  4  5]

# Array Addition
print(new_arr + new_arr)
# OUTPUT: [ 2  4  6  8 10 12 14 16 18 20]

# Array Division
print(new_arr / new_arr)
# OUTPUT:[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
