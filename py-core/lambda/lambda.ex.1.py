my_list = [2, 1, 0, -1, -2]
print(sorted(my_list))

# we can use a lambda function to define the key, which is what the sorted() method uses to determine how to sort.
print(sorted(my_list, key = lambda x : x ** 2))
