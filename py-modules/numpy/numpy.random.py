import numpy as np

print(np.random.rand(10))  # array

print(np.random.rand(3, 4))  # 3x4 matrix

# To generate random numbers in a normal distribution, use the randn() function from np.random:

print(np.random.randn(10))

print(np.random.randn(3, 4))

# To generate random integers between a low and high value, use the randint() function from np.random:

print(np.random.randint(1, 100, 10))

print(np.random.randint(1, 100, (2, 3)))

# To set a seed value in NumPy, do the following:

np.random.seed(42)
print(np.random.rand(4))
