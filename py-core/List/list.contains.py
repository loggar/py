games = ['Yankees', 'Yankees', 'Cubs', 'Blue Jays', 'Giants']


def contains(item, list_name):
    if item in list_name:
        print(f"{item} is in the list!")
    else:
        print(f"{item} is not in the list!")


contains('Blue Jays', games)
contains('Angels', games)

# Returns
# Blue Jays is in the list!
# Angels is not in the list!
