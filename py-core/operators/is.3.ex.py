# All right, now our class has a correct equality logic.
# The equality logic is implemented in __eq__ method.
# It is also implemented in Python built-in types like Integers.

import inspect
from pprint import pprint

# 1 is object of int class
pprint(inspect.getmembers(1))
pprint(inspect.getmembers(int))
