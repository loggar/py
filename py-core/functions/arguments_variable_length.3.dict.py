
"""
**kwargs are represented using dictionary data structure.
"""


def items(**kwargs):
    print(f"Type of **kwargs is {type(kwargs)}")  # print type of **kwargs
    # iterating over the keyword argument
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key} = {value}")


items(a="basket", b="plate", c="soap")
