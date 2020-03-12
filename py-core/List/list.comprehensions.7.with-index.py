li = ['a', 'b', 'c']
op = [f'{x}_{i}' for i, x in enumerate(li)]  # enum returns a list of tuples
print(op)

# Output: ['a_0', 'b_1', 'c_2']
