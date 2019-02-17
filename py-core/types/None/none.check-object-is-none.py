class MyClass:
    def __eq__(self, my_object):
        # We won't bother checking if my_object is actually equal
        # to this class, we'll lie and return True. This may occur
        # when there is a bug in the comparison class.

        return True


my_class = MyClass()

if my_class is None:
    print('my_class is None, using the is keyword')
else:
    print('my_class is not None, using the is keyword')

if my_class == None:
    print('my_class is None, using the == syntax')
else:
    print('my_class is not None, using the == syntax')
