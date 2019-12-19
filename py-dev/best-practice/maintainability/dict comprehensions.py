"""
numbers = [1,2,3]

# hard to read
my_dict = dict([(number,number*2) for number in numbers])

print(my_dict)  # {1: 2, 2: 4, 3: 6}
"""

numbers = [1, 2, 3]

my_dict = {number: number * 2 for number in numbers}

print(my_dict)  # {1: 2, 2: 4, 3: 6}
