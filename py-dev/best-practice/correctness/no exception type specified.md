# python anti-patterns

## No exception type(s) specified

- PyLint W0702, bare-except

Anti-pattern

```py
def divide(a, b):

    try:
        result = a / b
    except:
        result = None

    return result
```

Best practice (specify build-in exceptions)

```py
def divide(a, b):

    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        print("Type error: division by 0.")
    except TypeError:
        # E.g., if b is a string
        print("Type error: division by '{0}'.".format(b))
    except Exception as e:
        # handle any other exception
        print("Error '{0}' occured. Arguments {1}.".format(e.message, e.args))
    else:
        # Excecutes if no exception occured
        print("No errors")
    finally:
        # Executes always
        if result is None:
            result = 0

    return result
```

Implement user defined exceptions

```py
class DivisorTooSmallError(StandardError):
    def __init__(self, arg):
        self.args = arg


def divide(a, b):
    if b < 1:
        raise DivisorTooSmallError
    return a / b


try:
    divide(10, 0)
except DivisorTooSmallError:
    print("Unable to divide these numbers!")
```
