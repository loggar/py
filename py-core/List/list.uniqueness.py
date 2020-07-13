list1 = [1, 2, 3, 4, 5]
list2 = [1, 1, 2, 3, 4]


def isunique(list):
    if len(list) == len(set(list)):
        print('Unique!')
    else:
        print('Not Unique!')


isunique(list1)
isunique(list2)

# Returns
# Unique!
# Not Unique!
