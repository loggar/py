"""
Generator — memory efficiency
Generators are utilized when we intend to calculate a large set of results but would like to avoid allocating the memory needed for all results at the same time. In other words, they generate values on the fly and do not store previous values in memory, and thus we can only iterate over them once.
They are often used when reading large files or generating an infinite sequence using keyword yield. I often find it useful in most of my data science projects.
"""


def gen(n):    # an infinite sequence generator that generates integers >= n
    while True:
        yield n
        n += 1


G = gen(3)     # starts at 3
print(next(G))  # 3
print(next(G))  # 4
print(next(G))  # 5
print(next(G))  # 6
