class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


class Square(Rectangle):
    def __init__(self, length):
        # This is equivalent to super(Square, self).__init__(length, length)
        super().__init__(length, length)


s = Square(5)
print(s.area)  # 25
