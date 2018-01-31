dict_1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict_1['Age'] = 8  # update existing entry
dict_1['School'] = "DPS School"  # Add new entry

print("dict_1['Age']: ", dict_1['Age'])
print("dict_1['School']: ", dict_1['School'])


dict_2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict_2['Name']  # remove entry with key 'Name'
dict_2.clear()     # remove all entries in dict
del dict_2         # delete entire dictionary

#print("dict_2['Age']: ", dict_2['Age'])
#print("dict_2['School']: ", dict_2['School'])
