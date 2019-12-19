import types


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height


r = Rectangle(3, 4)

# good
if isinstance(r, types.ListType):
    print("object r is a list")
