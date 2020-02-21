# Split based on age
from datetime import datetime, timedelta
from more_itertools import partition

dates = [
    datetime(2015, 1, 15),
    datetime(2020, 1, 16),
    datetime(2020, 1, 17),
    datetime(2019, 2, 1),
    datetime(2020, 2, 2),
    datetime(2018, 2, 4)
]


def is_old(x): return datetime.now() - x < timedelta(days=30)


old, recent = partition(is_old, dates)
list(old)
#  [datetime.datetime(2015, 1, 15, 0, 0), datetime.datetime(2019, 2, 1, 0, 0), datetime.datetime(2018, 2, 4, 0, 0)]
list(recent)
#  [datetime.datetime(2020, 1, 16, 0, 0), datetime.datetime(2020, 1, 17, 0, 0), datetime.datetime(2020, 2, 2, 0, 0)]


# Split based on file extension
files = [
    "foo.jpg",
    "bar.exe",
    "baz.gif",
    "text.txt",
    "data.bin",
]

ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'gif', 'bmp', 'png')


def is_allowed(x): return x.split(".")[1] in ALLOWED_EXTENSIONS


allowed, forbidden = partition(is_allowed, files)
list(allowed)
#  ['bar.exe', 'text.txt', 'data.bin']
list(forbidden)
#  ['foo.jpg', 'baz.gif']
