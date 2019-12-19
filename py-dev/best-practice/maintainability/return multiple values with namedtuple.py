from collections import namedtuple


def get_name():
    name = namedtuple("name", ["first", "middle", "last"])
    return name("Richard", "Xavier", "Jones")


name = get_name()

# much easier to read
print(name.first, name.middle, name.last)
