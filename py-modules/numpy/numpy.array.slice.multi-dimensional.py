import numpy as np

my_matrix = np.random.randint(1, 30, (3, 3))
print(my_matrix)

"""
OUTPUT: [
[21  1 20]
[22 16 27]
[24 14 22]
]
"""

print(my_matrix[0])  # print a single row
# OUTPUT: [21  1 20]

print(my_matrix[0][0])  # print a single value or row 0, column 0
# OUTPUT: 21

print(my_matrix[0, 0])  # alternate way to print value from row0,col0
# OUTPUT: 21
