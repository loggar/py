none_obj = None
print(none_obj is None)

number_one = 1
print(number_one is 1)

# In Python, every object created will store a reference to it, like in the above code none_obj which is storing a reference to None, and number_one object is storing a reference to 1. Let’s examine how this is done by Python.

print(id(none_obj))
print(id(None))
print(id(number_one))
print(id(1))

# When you create a new variable that stores an object or value, this variable name stores a reference to it, so if you create another variable to store the same object, Python stores a pointer to this object instead of creating a new one.


class Number:
    def __init__(self, number):
        self.number = number

    def __eq__(self, another_number):
        if isinstance(another_number, Number):
            return self.number == another_number.number
        return self.number == another_number


a = Number(1)
b = a
print(id(a), id(b))
print(a is b)

# Technically speaking, when you check the identity, Python checks id(a) == id(b), which means:

# Do objects a and b refer to the same object? So the answer will be True if they refer to the same object.

# == : value equality
# is : same result of id()
