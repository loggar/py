#!/usr/bin/python3

# Open a file
fo = open("./dist/foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()
