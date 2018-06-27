#!/usr/bin/python3

try:
    fh = open("./dist/testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()


try:
    fh = open("./dist/testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")

# The try-finally Clause

try:
    fh = open("./dist/testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print("Error: can\'t find file or read data")
    fh.close()


try:
    fh = open("./dist/testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")


# argument of an exception

# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)


# Call above function here.
temp_convert("xyz")


# raising an exception

def functionName(level):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level


def functionName2(level):
    if level < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
    return level


try:
    l = functionName2(-10)
    print("level = ", l)
except Exception as e:
    print("error in level argument", e.args[0])
