content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}


def make_percentages(a_dictionary):
    total = 0
    for key in a_dictionary:
        count = a_dictionary[key]
        total += count

    for key in a_dictionary:
        a_dictionary[key] = (a_dictionary[key] / total) * 100

    return a_dictionary


c_ratings_percentages = make_percentages(
    content_ratings.copy())  # making a copy of the dictionary
print(c_ratings_percentages)
print(content_ratings)
