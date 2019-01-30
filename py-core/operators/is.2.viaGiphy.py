class Number:
    def __init__(self, number):
        self.number = number

    def __eq__(self, another_number):
        if isinstance(another_number, Number):
            return self.number == another_number.number
        return self.number == another_number


print(Number(1) == Number(1))
print(Number(1) == 1)

# __init__() is dunder method to initiate a new object or the class constructor.
# For our example above, there is a dunder method used to check the equality which is __eq__() S,
# if we implement it correctly, the expression in the code about should work.
