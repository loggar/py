class Foo():
    def __init__(self, x):
        self.x = x
        self.y = None


f = Foo(10)
f.y = 'abcd'
print(vars(f))

# From Python's perspective, there isn't any issue. But you might like to say that both x and y must be integers, except for when y is initialized and set to None
