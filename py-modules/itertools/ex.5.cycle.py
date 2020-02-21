# Cycling through players
import time
from itertools import cycle

players = ["John", "Ben", "Martin", "Peter"]

next_player = cycle(players).__next__
player = next_player()
#  "John"

player = next_player()
#  "Ben"
#  ...

# Infinite Spinner

for c in cycle('/-\|'):
    print(c, end='\r')
    time.sleep(0.2)
