tuples = [('A', 'Good'), ('C', 'Faulty'), ('E', 'Pristine')]
something = [[key+' is '+val] for key, val in tuples if val != 'Faulty']
print(something)

# Output: [['A is Good'], ['E is Pristine']]
