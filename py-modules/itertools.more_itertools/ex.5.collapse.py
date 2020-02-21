import more_itertools
import os

# Get flat list of all files and directories
list(more_itertools.collapse(list(os.walk("/home/martin/Downloads"))))

# Get all nodes of tree into flat list
# [Root, SUB_TREE_1, SUB_TREE_2, ..., SUB_TREE_n]
tree = [40, [25, [10, 3, 17], [32, 30, 38]], [78, 50, 93]]
list(more_itertools.collapse(tree))
