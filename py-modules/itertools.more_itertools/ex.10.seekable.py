from more_itertools import seekable

data = "This is example sentence for seeking back and forth".split()

it = seekable(data)
for word in it:
    ...

next(it)
# StopIteration
it.seek(3)
next(it)
# "sentence"
