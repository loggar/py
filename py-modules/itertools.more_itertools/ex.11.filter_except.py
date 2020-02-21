from more_itertools import filter_except

data = ['1.5', '6', 'not-important', '11',
        '1.23E-7', 'remove-me', '25', 'trash']
list(map(float, filter_except(float, data, TypeError, ValueError)))
#  [1.5, 6.0, 11.0, 1.23e-07, 25.0]
