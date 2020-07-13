nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [i for j in nested_list for i in j]

print(flat_list)

# Returns [1, 2, 3, 4, 5, 6, 7, 8, 9]
