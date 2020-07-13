negative_numbers = filter(lambda x: x < 0, range(-5, 5))

print(list(negative_numbers))
# Output: [-5, -4, -3, -2, -1]


def filter_three(number):
    return number > 3


original_list = [1, 2, 3, 4, 5]

filtered = filter(filter_three, original_list)

print(list(filtered))
# Returns [4,5]
