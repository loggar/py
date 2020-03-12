iterator = (item for item in ['a', 'b', 'c'])  # defined by round brackets
result = next(iterator)
result = next(iterator)
iterator.close()
print(result)

# Output: b
