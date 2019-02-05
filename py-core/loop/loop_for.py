#!/usr/bin/python3

for letter in 'Python':     # traversal of a string sequence
    print('Current Letter :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:        # traversal of List sequence
    print('Current fruit :', fruit)



numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13]

for num in numbers:
    if num % 2 == 0:
        print('the list contains an even number')
        break
else:
    print('the list doesnot contain even number')
