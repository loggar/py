"""
Generator functions can be used within other functions
"""
a = range(6)
print("Generator expression", end=':n')
c = (x+2 for x in a)
print(c)
print(min(c))
