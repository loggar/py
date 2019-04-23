import numpy as np

array = np.asarray([7, 8])

# shape: To find the dimensions (numbers of column/row) of an array:
array.shape
array.shape = (1, 2)  # 1 row, 2 columns

# resize(x,y) can also be used to resize an array

# If you want to find the number of dimensions of an array:
array.dim

# If you want to find length of each element of an array:
array.itemsize
# It will then return the length of an element in bytes.

# If you want to slice a subset of an array:
array = np.arange(100)
# Get 3rd element:
array[2]
# Get items within indexes
array[3:5]  # 3 is start, 5 is end
# Get 3-10 element, step size 4 increments:
array[2:9:4]
# Get all elements from 2nd element onwards
array[1:]
# Can also pass in N-Dimensional Index
array[[0, 1], [1, 2]]


# Conditions In Array Slicing
array[np.isnan(array)]


# where() can be used to pass in boolean expressions:
np.where(array > 5)  # will return all elements that meet the criteria


# Broadcasting an array
# When a mathematical operation is performed on two arrays of different sizes then the smaller array is broadcasted to the size of the larger array:
bigger_array = arange(5, 3)  # 5 rows, 3 columns array
smaller_array = arange(5)  # 5 rows, 1 column array
final_array = bigger_array + smaller_array


# Transposing Array
array.T
# rollaxis, swapaxes, transpose are also available transpose functions.

# To join arrays:
a = np.asarray([7, 8])
b = np.asarray([1, 3])

np.concatenate(a, b)
np.stack(a, b)
np.hstack(a, b)
np.vstack(a, b)


# String Operations
# add(), upper(), lower(), replace() etc.


# To create a deep copy of numpy array:
new_array = np.copy(array)
