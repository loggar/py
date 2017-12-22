list1 = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list1)          # Prints complete list
print(list1[0])       # Prints first element of the list
print(list1[1:3])     # Prints elements starting from 2nd till 3rd
print(list1[2:])      # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list1 + tinylist)  # Prints concatenated lists


# Updating Lists

list2 = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ", list2[2])

list2[2] = 2001
print("New value available at index 2 : ", list2[2])


# Delete List Elements

list3 = ['physics', 'chemistry', 1997, 2000]

print(list3)
del list3[2]
print("After deleting value at index 2 : ", list3)


# Basic List Operations
'''
len([1, 2, 3])	3	Length
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
for x in [1,2,3] : print (x,end = ' ')	1 2 3	Iteration
'''

# Indexing, Slicing and Matrixes
'''
L[2]	'Python'	Offsets start at zero
L[-2]	'Java'	Negative: count from the right
L[1:]	['Java', 'Python']	Slicing fetches sections
'''
