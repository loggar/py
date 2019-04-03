lst = [1, 3, 5]
doubled = []
for num in lst:
    doubled.append(num*2)

print(doubled)

# list map
doubled = [num * 2 for num in lst]

print(doubled)
