def stupid_func(x):
    return x**2 + 5


my_list = [1, 2, 3, 4, 5]

# without list comprehensions
new_list = []
for x in my_list:
    if x % 2 != 0:
        new_list.append(stupid_func(x))
print(new_list)

# list comprehensions
new_list2 = [stupid_func(x) for x in my_list if x % 2 != 0]
print(new_list2)

# function to expression
new_list3 = [x ** 2 + 5 for x in my_list if x % 2 != 0]
print(new_list3)
