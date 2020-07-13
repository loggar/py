original_list = [1, 2, 3, 4, 5]


def square(number):
    return number ** 2


squares = map(square, original_list)

squares_list = list(squares)

print(squares)

# Returns [1, 4, 9, 16, 25]
