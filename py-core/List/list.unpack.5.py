another_str = "The * operator"

# Using a list outside the unpacking
var2 = [*another_str]

print(type(var2))  # List

# Using a tuple
# Tuples ends with a comma
var3 = (*another_str,)

print(type(var3))  # Tuple
