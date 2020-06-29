from collections import Counter

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(Counter(test).most_common(1))
