import numpy as np

array = np.asarray([1, 2, 3, 4, 5])
array1 = np.asarray([7, 8])
array2 = np.asarray([1, 3])

# Add, Subtract, Multiple, Divide, Power, Mod

np.add(array1, array2)
np.subtract(array1, array2)
np.multiply(array1, array2)
np.divide(array1, array2)
np.pow(array1, array2)
np.pow(array1, integer)
# to get remainder
np.mod(array1, array2)
np.remainder(array1, array2)


# Rounding, Ceil, Floor

np.around(array, 4)  # 4dp
np.ceil(array)  # 1.8 will become 2
np.floor(array)  # 1.8 will become 1


# Trigonometric

array = np.arange(10)
np.sin(array)
np.cos(array)
np.tan(array)
np.arcsin(array)
np.arcos(array)
np.arctan(array)


# Statistical

np.amin(array1, axis)  # min in the axis
np.amax(array1, axis)  # max in the axis
np.percentile(array1, percentile)
# Additionally, following functions are available:
np.median(), np.st(), np.average(), np.mean(), np.var()


# Algebra

# 1. dot() #dot product of two arrays
# 2. inner() #inner product of two arrays
# 3. determinant() #determinant of an array
# 4. solve() #solves matrix equation
# 5. inv() #inverse of matrix
# 6. matmul() #matrix product of two arrays
