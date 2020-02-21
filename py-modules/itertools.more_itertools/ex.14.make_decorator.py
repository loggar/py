from more_itertools import make_decorator
from more_itertools import map_except

mapper_except = make_decorator(map_except, result_index=1)


@mapper_except(float, ValueError, TypeError)
def read_file(f):
    ...  # Read mix of text and numbers from file
    return ['1.5', '6', 'not-important', '11', '1.23E-7', 'remove-me', '25', 'trash']


list(read_file("file.txt"))
#  [1.5, 6.0, 11.0, 1.23e-07, 25.0]
