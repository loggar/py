from math import sqrt

number = 0

for i in range(10):
    number = i ** 2

    if i % 2 == 0:
        continue    # continue here

    print(str(round(sqrt(number))) + ' squared is equal to ' + str(number))
