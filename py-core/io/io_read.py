#!/usr/bin/python3

# Open a file
fo = open("./dist/foo.txt", "r+")
s = fo.read(10)
s2 = fo.read()
print(s)
print(s2)

# Close opened file
fo.close()
