#!/usr/bin/python3

for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current Letter :', letter)

"""
pass is a null operation -- when it is executed, nothing happens. It is useful as a placeholder when a statement is required syntactically, but no code needs to be executed, for example:

def f(arg): pass    # a function that does nothing (yet)

class C: pass       # a class with no methods (yet)
"""
