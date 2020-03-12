items = [1, 2, 3, 4, 5]
map_obj = map(lambda x: x**2, items)  # returns iterable object
print(list(map_obj))  # use list to iterate

# Output: [1, 4, 9, 16, 25]
