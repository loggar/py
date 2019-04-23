import numpy as numpy

a = numpy.array([1, 2, 3])

numpy.array([1, 2])  # 1D
numpy.array([[1, 2], [10, 20]])  # 2D
# For complex types
numpy.array([1, 2], dtype=complex)  # 1D comple

a3dArray = numpy.random.randint(10, size=(3, 4, 5))

print(a3dArray)
