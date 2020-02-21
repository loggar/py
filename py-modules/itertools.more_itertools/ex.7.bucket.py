# Split based on Object Type
import more_itertools


class Cube:
    pass


class Circle:
    pass


class Triangle:
    pass


shapes = [Circle(), Cube(), Circle(), Circle(), Cube(), Triangle(), Triangle()]
s = more_itertools.bucket(shapes, key=lambda x: type(x))
# s -> <more_itertools.more.bucket object at 0x7fa65323f210>
list(s[Cube])
#  [<__main__.Cube object at 0x7f394a0633c8>, <__main__.Cube object at 0x7f394a063278>]
list(s[Circle])
# [<__main__.Circle object at 0x7f394a063160>, <__main__.Circle object at 0x7f394a063198>, <__main__.Circle object at 0x7f394a063320>]
