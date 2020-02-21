# Consecutive Groups of dates
import datetime
import more_itertools

dates = [
    datetime.datetime(2020, 1, 15),
    datetime.datetime(2020, 1, 16),
    datetime.datetime(2020, 1, 17),
    datetime.datetime(2020, 2, 1),
    datetime.datetime(2020, 2, 2),
    datetime.datetime(2020, 2, 4)
]

ordinal_dates = []
for d in dates:
    ordinal_dates.append(d.toordinal())

groups = [list(map(datetime.datetime.fromordinal, group))
          for group in more_itertools.consecutive_groups(ordinal_dates)]
