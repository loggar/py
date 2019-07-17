x = {'u': 4, 'w': 2, 'v': 1}

print(sorted(x.items()))
print(sorted(x.items(), key=lambda item: item[1]))
print(sorted(x.items(), key=lambda item: item[1], reverse=True))
