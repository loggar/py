"""module docstring."""

str1 = 'this is a literal string'
str2 = "this is another string"
str3 = 'this is a literal string'
str4 = "this is another string"

big = "This is a long string\
that spans two lines."

big2 = "This is a long string\n\
that prints on two lines."

bigger = """
This is an even
bigger string that
spans three lines.
"""
biggerR = r"raw string : This is a long string\
with a backslash and a newline in it"

hello = u'Hello\u0020World'

print(big)
print(big2)
print(bigger)
print(biggerR)
print(hello)

mystr = str("my string")
print(mystr[0])  # 'm'
print(mystr[-2])  # 'n'

print(mystr[1:4])  # 'y s'
print(mystr[3:])  # 'string'
print(mystr[-3:])  # 'ing'
print(mystr[:3:-1])  # 'gnirt'
print(mystr[1::2])  # 'ysrn'

for c in mystr:
    print(c)

print(list(mystr))  # ['m','y',' ','s','t','r','i','n','g']
print(mystr + 'oid')  # my stringoid
print(mystr * 3)  # my stringmy stringmy string
