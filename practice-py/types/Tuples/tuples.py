tuple1 = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple1)           # Prints complete tuple
print(tuple1[0])        # Prints first element of the tuple
print(tuple1[1:3])      # Prints elements starting from 2nd till 3rd
print(tuple1[2:])       # Prints elements starting from 3rd element
print(tinytuple * 2)   # Prints tuple two times
print(tuple1 + tinytuple)  # Prints concatenated tuple

list1 = ['abcd', 786, 2.23, 'john', 70.2]
# tuple1[2] = 1000    # Invalid syntax with tuple
list1[2] = 1000     # Valid syntax with list
