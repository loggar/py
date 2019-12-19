class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._area = width * height
    # instance members now accessible because of "self"

    @property
    def area(self):
        return self._area

    @classmethod
    # class members now accessible, thanks to "cls"
    def print_class_name(cls):
        print("Hello, I am {0}!".format(cls))

    # clarifies that the method does not need any instance members
    @staticmethod
    def static_area(width, height):
        return width * height
