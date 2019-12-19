"""
The exec statement enables you to dynamically execute arbitrary Python code which is stored in literal strings. Building a complex string of Python code and then passing that code to exec results in code that is hard to read and hard to test. Anytime the Use of exec error is encountered, you should go back to the code and check if there is a clearer, more direct way to accomplish the task.

Program uses exec to execute arbitrary Python code

The sample code below composes a literal string containing Python code and then passes that string to exec for execution. This is an indirect and confusing way to program in Python.

s = "print(\"Hello, World!\")"
exec s

Refactor the code to avoid exec

In most scenarios, you can easily refactor the code to avoid the use of exec. In the example below, the use of exec has been removed and replaced by a function.

"""


def print_hello_world():
    print("Hello, World!")


print_hello_world()
