class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email


tk = Person('TK', 'tk@mail.com')
# print(tk._email) # tk@mail.com
# [pylint] W0212:Access to a protected member _email of a client class

"""
We can access and update it. Non-public variables are just a convention and should be treated as a non-public part of the API.
"""
