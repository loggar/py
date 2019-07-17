x = [2, 1, 4, 16, 8]
i = max((item, i) for i, item in enumerate(x))[1]
print(i)  # 3

# If there are two or more elements with the maximal value, this approach returns the index of the last one:
y = [2, 1, 4, 8, 8]
j = max((item, i) for i, item in enumerate(y))[1]
print(j)  # 4

# To get the index of the first occurrence, you need to change the previous statement slightly:
j = -max((item, -i) for i, item in enumerate(y))[1]
print(j)  # 3

# The alternative way is probably more elegant:
print(max(range(len(x)), key=lambda i: x[i]))  # 3
print(max(range(len(y)), key=lambda i: x[i]))  # 3
