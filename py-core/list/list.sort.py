x = (1, 'v')
y = (4, 'u')
z = (2, 'w')

print(sorted([x, y, z]))
print(sorted([x, y, z], key=lambda item: item[1]))
print(sorted([x, y, z], key=lambda item: item[1], reverse=True))
