# Define a generic 1D list of constants
my_list = [2, 5, -4, 6]

# Duplicate a 1D list of constants
[item for item in my_list]

# Duplicate and scale a 1D list of constants
[2 * item for item in my_list]

# Duplicate and filter out non-negatives from 1D list of constants
[item for item in my_list if item < 0]

# Duplicate, filter, and scale a 1D list of constants
[2 * item for item in my_list if item < 0]

# Generate all possible pairs from two lists
[(a, b) for a in (1, 3, 5) for b in (2, 4, 6)]

# Redefine list of contents to be 2D
my_list = [[1, 2], [3, 4]]

# Duplicate a 2D list
[[item for item in sub_list] for sub_list in my_list]

# Duplicate an n-dimensional list


def deep_copy(to_copy):
    if type(to_copy) is list:
        return [deep_copy(item) for item in to_copy]
    else:
        return to_copy
