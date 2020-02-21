from more_itertools import map_reduce
data = 'This sentence has words of various lengths in it, both short ones and long ones'.split()


def keyfunc(x): return len(x)


result = map_reduce(data, keyfunc)
# defaultdict(None, {
#   4: ['This', 'both', 'ones', 'long', 'ones'],
#   8: ['sentence'],
#   3: ['has', 'it,', 'and'],
#   5: ['words', 'short'],
#   2: ['of', 'in'],
#   7: ['various', 'lengths']})


def valuefunc(x): return 1


result = map_reduce(data, keyfunc, valuefunc)
# defaultdict(None, {
#   4: [1, 1, 1, 1, 1],
#   8: [1],
#   3: [1, 1, 1],
#   5: [1, 1],
#   2: [1, 1],
#   7: [1, 1]})

reducefunc = sum
result = map_reduce(data, keyfunc, valuefunc, reducefunc)
# defaultdict(None, {
#   4: 5,
#   8: 1,
#   3: 3,
#   5: 2,
#   2: 2,
#   7: 2})
