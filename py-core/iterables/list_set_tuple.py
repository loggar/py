"""
lists are for iterables that should be ordered and mutable.
sets are for iterables that should only contain unique values and are mutable and unordered. They should be preferred when checking for the presence of an item, in which they are extremely fast. However, they are slower than a list when used to iterate over.
tuples are for iterables that should be ordered and immutable. Tuples are faster and more memory-efficient than lists.
"""

requested_usernames = ["John123", "Delilah42"]
taken_usernames = set()
for username in requested_usernames:
    if username not in taken_usernames:
        taken_usernames.add(username)
    else:
        print(f"Username '{username}' is already taken!")

# more junior example
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day in weekdays:
    print(day)

# more senior example
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for day in WEEKDAYS:
    print(day)
