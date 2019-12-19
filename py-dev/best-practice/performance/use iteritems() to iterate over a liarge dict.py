"""
d = {i: i * 2 for i in xrange(10000000)}

# Slow and memory hungry.
for key, value in d.items():
    print("{0} = {1}".format(key, value))
"""

d = {i: i * 2 for i in xrange(10000000)}

# Memory efficient.
for key, value in d.iteritems():
    print("{0} = {1}".format(key, value))
