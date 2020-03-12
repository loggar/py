numbers = [1, 2, 3, 4]
list_comp = [n**2 for n in numbers if n%2 == 0 and n**n > 10]
print(list_comp)

# Output: [16]