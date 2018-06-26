#!/usr/bin/python3

# Open a file
fo = open("./dist/foo.txt", "r+")
s = fo.read(10)
print("Read String is : ", s)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
s2 = fo.read(10)
print("Again read String is : ", s2)

# Close opened file
fo.close()
