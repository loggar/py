"""
We can also use * to collect values during an assignment.
"""

first, *others = ["first", "second", "third"]
print(first, others, sep="\n")
