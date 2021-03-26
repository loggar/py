import numpy as np

array = np.asarray([1, 2, 5, 7, 0, 4])

np.append(array, [1, 2])  # adds 1,2 at the end
# insert can also be used if we want to insert along a given index

np.delete(array, 1)  # 1 is going to be deleted from the array

np.sort(array, axis=1, kind='quicksort', order='column name')
