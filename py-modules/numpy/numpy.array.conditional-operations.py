import numpy as np

arr = np.arange(0, 10)
# OUTPUT: [0,2,3,4,5,6,7,8,9]

print(arr > 4)
# OUTPUT: [False False False False False  True  True  True  True  True]

print(arr[arr > 4])
# OUTPUT: [5 6 7 8 9]
