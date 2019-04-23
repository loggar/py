import numpy as numpy

# If you want to create an array without any element:
numpy.empty(2)  # this will create 1D array of 2 elements
numpy.empty(2, 3)  # this will create 2D array (2 rows, 3 columns each)

# If you want to create an array with 0s:
numpy.zeros(2)  # it will create an 1D array with 2 elements, both 0
# Note the parameter of the method is shape, it could be int or a tuple

# If you want to create an array with 1s:
numpy.ones(2)  # this will create 1D array with 2 elements, both 1

# If you want to create a Numpy array from Python sequence of elements:
# numpy.asarray([python sequence]) str, unicode, list, tuple, buffer, xrange
numpy.asarray([1, 2])

# A text can be created as an array:
numpy.frombuffer('hi')
# frombuffer() takes in any object that exposes buffer interface

# If you want to create a range of elements:
array = numpy.arange(3)
# array will contain 0,1,2

# If you want to create an array with values that are evenly spaced:
# numpy.arange(first, last, step, type)
# without last, step and type, the function behaves like arange()
# e.g. to create 0-5, 2 apart
numpy.array(0, 6, 2)
# will return [0, 2, 4]


# If you want to create an array where the values are linearly spaced between an interval then use:
# numpy.linspace(first, last, number)
numpy.linspace(0, 10, 5)
# will return [0,2.5,5,7.5,10]


# If you want to create an array where the values are log spaced between an interval then use:
# numpy.logspace(first, end, number)


# Random number generation
numpy.random.rand(3, 2)  # 3 rows, 2 cols
