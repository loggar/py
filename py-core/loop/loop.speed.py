import timeit

"""
The Fastest Way to Loop in Python - An Unfortunate Truth
https://www.youtube.com/watch?app=desktop&v=Qgevy75co8c
"""

def while_loop(n=10_000_000):
    s = 0
    i = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n=10_000_000):
    s = 0
    for i in range(n):  # written in c
        s += i
    return s


def main():
    print("while loop: ", timeit.timeit(while_loop, number=1))
    print("for   loop: ", timeit.timeit(for_loop, number=1))


if __name__ == '__main__':
    main()
