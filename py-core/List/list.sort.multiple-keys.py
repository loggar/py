import operator

people = [
    {'name': 'John', "age": 64},
    {'name': 'Janet', "age": 34},
    {'name': 'Ed', "age": 24},
    {'name': 'Sara', "age": 64},
    {'name': 'John', "age": 32},
    {'name': 'Jane', "age": 34},
    {'name': 'John', "age": 99},
]

people.sort(key=operator.itemgetter('age'))
people.sort(key=operator.itemgetter('name'))

print(people)
