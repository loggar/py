from itertools import accumulate
import operator

data = [3, 4, 1, 3, 5, 6, 9, 0, 1]

list(accumulate(data, max))  # running maximum
#  [3, 4, 4, 4, 5, 6, 9, 9, 9]

list(accumulate(range(1, 11), operator.mul))  # Factorial
#  [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
