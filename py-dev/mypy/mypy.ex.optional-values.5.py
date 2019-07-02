from typing import Optional


class Foo():
    def __init__(self, x: int):
        self.x: int = x
        self.y: Optional[int] = None


f = Foo(10)
f.y = 'abcd'
print(vars(f))

# mypy.ex.optional-values.5.py:11: error: Incompatible types in assignment (expression has type "str", variable has type "Optional[int]")
