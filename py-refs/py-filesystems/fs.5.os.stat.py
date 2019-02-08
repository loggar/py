import os

stat_dir = os.stat('.')

print(stat_dir)

stat_file = os.stat('./readme.md')

print(stat_file)

# https://docs.python.org/3/library/os.html#os.stat_result
