import numpy as np

# To get the shape of an array, use the shape property.

arr = np.random.rand(2, 2)
print(arr)
print(arr.shape)

# To reshape an array, use the reshape() function.

print(arr.reshape(1, 4))
OUTPUT: [[0.19890857 0.00806693 0.48199837 0.55373954]]
print(arr.reshape(4, 1))
