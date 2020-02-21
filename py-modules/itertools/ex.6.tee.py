from itertools import tee


def pairwise(iterable):
    """
    s -> (s0, s1), (s1, s2), (s2, s3), ...
    """
    a, b = tee(iterable, 2)
    next(b, None)
    return zip(a, b)
