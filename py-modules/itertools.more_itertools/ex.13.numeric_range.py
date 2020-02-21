from more_itertools import numeric_range
import datetime
from decimal import Decimal

list(numeric_range(Decimal('1.7'), Decimal('3.5'), Decimal('0.3')))
#  [Decimal('1.7'), Decimal('2.0'), Decimal('2.3'), Decimal('2.6'), Decimal('2.9'), Decimal('3.2')]

start = datetime.datetime(2020, 2, 10)
stop = datetime.datetime(2020, 2, 15)
step = datetime.timedelta(days=2)
list(numeric_range(start, stop, step))
#  [datetime.datetime(2020, 2, 10, 0, 0), datetime.datetime(2020, 2, 12, 0, 0), datetime.datetime(2020, 2, 14, 0, 0)]
