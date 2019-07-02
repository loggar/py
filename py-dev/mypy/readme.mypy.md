# mypy

```
pip3 install mypy
```

`mypy.ex.1.py`

```py
def hello(name:str):
   return f"Hello, {name}"


print(hello('world'))
print(hello(5))
print(hello([10, 20, 30]))
```

```
(.venv) mypy ./mypy.ex.1.py
mypy.ex.1.py:6: error: Argument 1 to "hello" has incompatible type "int"; expected "str"
mypy.ex.1.py:7: error: Argument 1 to "hello" has incompatible type "List[int]"; expected "str"
```

`mypy.ex.2.py`

```py
def hello(name: str) -> str:
    return f"Hello, {name}"


print(hello('world'))
print(hello(5))
print(hello([10, 20, 30]))
```

```
(.venv) mypy ./mypy.ex.2.py
mypy.ex.2.py:6: error: Argument 1 to "hello" has incompatible type "int"; expected "str"
mypy.ex.2.py:7: error: Argument 1 to "hello" has incompatible type "List[int]"; expected "str"
```

`mypy.ex.3.py`

```py
def mysum(numbers: list) -> int:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10, 20, 30, 40, 50)))
print(mysum([10, 20, 'abc', 'def', 50]))
print(mysum('abcd'))
```

```
(.venv) mypy ./mypy.ex.3.py
mypy.ex.3.py:9: error: Argument 1 to "mysum" has incompatible type "Tuple[int, int, int, int, int]"; expected "List[Any]"
mypy.ex.3.py:11: error: Argument 1 to "mysum" has incompatible type "str"; expected "List[Any]"
```

The good news is that I've identified some problems. But in one case, I'm calling `mysum` with a tuple of numbers, which should be fine, but is flagged as a problem. And in another case, I'm calling it with a list of both integers and strings, but that's seen as just fine.

I'm going to need to tell `mypy` that I'm willing to accept not just a list, but any sequence, such as a tuple. Fortunately, Python now has a `typing` module that provides you with objects designed for use in such circumstances.

`mypy.ex.4.py`

```py
from typing import Sequence


def mysum(numbers: Sequence) -> int:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10, 20, 30, 40, 50)))
print(mysum([10, 20, 'abc', 'def', 50]))
print(mysum('abcd'))
```

```
(.venv) mypy ./mypy.ex.4.py
# mypy problems disappear, because all of the arguments are sequences
# What I really want to say is that I'll accept any sequence whose elements are integers
```

I can state that by changing my function's annotations to be:

`mypy.ex.5.py`

```py
from typing import Sequence


def mysum(numbers: Sequence[int]) -> int:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10, 20, 30, 40, 50)))
print(mysum([10, 20, 'abc', 'def', 50]))
print(mysum('abcd'))
```

```
(.venv) mypy ./mypy.ex.5.py
mypy.ex.5.py:13: error: List item 2 has incompatible type "str"; expected "int"
mypy.ex.5.py:13: error: List item 3 has incompatible type "str"; expected "int"
mypy.ex.5.py:14: error: Argument 1 to "mysum" has incompatible type "str"; expected "Sequence[int]"
```

But wait: do I really only want to allow for lists and tuples? What about sets, which also are iterable and can contain integers? And besides, what's this obsession with integers - shouldn't I also allow for floats?

I can solve the first problem by saying that I'll take not a `Sequence[int]`, but `Iterable[int]` - meaning, anything that is iterable and returns integers. In other words, I can say:

`mypy.ex.6.py`

```py
from typing import Iterable


def mysum(numbers: Iterable[int]) -> int:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10, 20, 30, 40, 50)))
print(mysum([10, 20, 'abc', 'def', 50]))
print(mysum('abcd'))
```

```
(.venv) mypy ./mypy.ex.6.py
mypy.ex.6.py:13: error: List item 2 has incompatible type "str"; expected "int"
mypy.ex.6.py:13: error: List item 3 has incompatible type "str"; expected "int"
mypy.ex.6.py:14: error: Argument 1 to "mysum" has incompatible type "str"; expected "Iterable[int]"
mypy.ex.6.py:14: note: Following member(s) of "str" have conflicts:
mypy.ex.6.py:14: note:     Expected:
mypy.ex.6.py:14: note:         def __iter__(self) -> Iterator[int]
mypy.ex.6.py:14: note:     Got:
mypy.ex.6.py:14: note:         def __iter__(self) -> Iterator[str]
```

Finally, how can I allow for either integers or strings? I use the special `Union` type, which lets you combine types together in square brackets:

`mypy.ex.7.py`

```py
from typing import Iterable, Union


def mysum(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10.1, 20.2, 30.3, 40, 50)))
```

```
(.venv) mypy ./mypy.ex.7.py
mypy.ex.7.py:7: error: Incompatible types in assignment (expression has type "float", variable has type "int")
```

What's the problem? Simply put, when I create `output` as a variable, I'm giving it an integer value. And then, when I try to add a floating-point value to it, I get a warning from `mypy`. So, I can silence that by annotating the variable:

`mypy.ex.8.py`

```py
from typing import Iterable, Union


def mysum(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
    output: Union[int, float] = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10.1, 20.2, 30.3, 40, 50)))
```

```
(.venv) mypy ./mypy.ex.8.py
# The function is now pretty well annotated.
```
