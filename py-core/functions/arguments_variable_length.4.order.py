# right
def my_func(argvs, *args, **kwargs):
    pass


# wrong
def my_func2(argvs, **kwargs, *args):
    pass


"""
The correct order for your parameters is:
standard arguments
*args arguments
**kwargs arguments
"""
