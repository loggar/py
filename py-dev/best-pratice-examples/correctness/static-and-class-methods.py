class Rectangle:
    # clarifies that this is a static method and belongs here
    @staticmethod
    def area(width, height):
        return width * height

    @classmethod
    def print_class_name(cls):
        # "class name: Rectangle"
        print("class name: {0}".format(cls))
