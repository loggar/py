from functools import cmp_to_key
import locale
my_list = ["leaf", "cherry", "fish"]

# Brute force method using bubble sort
my_list = ["leaf", "cherry", "fish"]
size = len(my_list)
for i in range(size):
    for j in range(size):
        if my_list[i] < my_list[j]:
            temp = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = temp

# Generic list sort *fastest*
my_list.sort()

# Casefold list sort
my_list.sort(key=str.casefold)

# Generic list sorted
my_list = sorted(my_list)

# Custom list sort using casefold (>= Python 3.3)
my_list = sorted(my_list, key=str.casefold)

# Custom list sort using current locale
my_list = sorted(my_list, key=cmp_to_key(locale.strcoll))

# Custom reverse list sort using casefold (>= Python 3.3)
my_list = sorted(my_list, key=str.casefold, reverse=True)
