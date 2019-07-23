import numpy as np

np.random.seed(0)  # seed for reproducibility
x = np.random.randint(10, size=6)
y = np.random.randint(10, size=6)

for val in x:
    print(val)

# creating our 2-dimensional array
z = np.array([x, y])

for val in z:
    print(val)

# each element for 2-dimentsional array
for val in np.nditer(z):
    print(val)
