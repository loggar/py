def outer():
    x = 1

    def inner():
        print(f'x in outer function (before modifying): {x}')
        x += 1
        print(f'x in outer function (after modifying): {x}')
    return inner
