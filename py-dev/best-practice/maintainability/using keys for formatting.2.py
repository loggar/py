class Person(object):

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return '{first} {last} is {age} years old'.format(**self.__dict__)


person = Person('Tobin', 'Brown', 20)
print(person)
# Output: Tobin Brown is 20 years old
