def positions(first_arg, *args):
    print(f"Type of *args is {type(args)}")  # print type of args
    print(f"first position arg:{first_arg}")
    for arg in args:
        print(f"another arg through *args: {arg}")


positions('first', 'second', 'third', 'forth')
