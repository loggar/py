# When duplicate keys are encountered during assignment, the last assignment wins

dict_1 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print("dict_1['Name']: ", dict_1['Name'])

# Keys must be immutable

dict_2 = {['Name']: 'Zara', 'Age': 7}
# print("dict_2['Name']: ", dict_2['Name'])
# TypeError: list objects are unhashable

