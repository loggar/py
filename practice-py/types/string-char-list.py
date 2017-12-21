str1 = "some string"


def do_something_with_char(arg):
    print(arg)
    return arg.upper()


do_something_with_char("c")


listChar = list(str1)
print(listChar)

for c in str1:
    do_something_with_char(c)

result1 = [do_something_with_char(c) for c in str1]
print(result1)

result2 = map(do_something_with_char, str1)
print(result2)
