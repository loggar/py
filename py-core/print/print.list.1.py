row = ["1", "bob", "developer", "python"]

print(row)
print(','.join(str(x) for x in row))
print(*row, sep=',')
