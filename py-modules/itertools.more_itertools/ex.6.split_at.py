import more_itertools

lines = [
    "erhgedrgh",
    "erhgedrghed",
    "esdrhesdresr",
    "ktguygkyuk",
    "-------------",
    "srdthsrdt",
    "waefawef",
    "ryjrtyfj",
    "-------------",
    "edthedt",
    "awefawe",
]

list(more_itertools.split_at(lines, lambda x: '-------------' in x))
#  [['erhgedrgh', 'erhgedrghed', 'esdrhesdresr', 'ktguygkyuk'], ['srdthsrdt', 'waefawef', 'ryjrtyfj'], ['edthedt', 'awefawe']]
