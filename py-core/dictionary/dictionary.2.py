dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}


# key-value pairs
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}

print("My name is %s" % (dictionary_tk["name"]))  # My name is Leandro
print("But you can call me %s" %
      (dictionary_tk["nickname"]))  # But you can call me Tk
# And by the way I'm Brazilian
print("And by the way I'm %s" % (dictionary_tk["nationality"]))


# we can use anything as the value. In the Dictionary I created, I want to add the key “age” and my real integer age in it:
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian",
    "age": 24
}

print("My name is %s" % (dictionary_tk["name"]))  # My name is Leandro
print("But you can call me %s" %
      (dictionary_tk["nickname"]))  # But you can call me Tk
print("And by the way I'm %i and %s" % (
    dictionary_tk["age"], dictionary_tk["nationality"]))  # And by the way I'm Brazilian


# add elements
dictionary_tk = {
    "name": "Leandro",
    "nickname": "Tk",
    "nationality": "Brazilian"
}

dictionary_tk['age'] = 24

print(dictionary_tk)
# {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}


# iterate dictionary
dictionary = {"some_key": "some_value"}

for key in dictionary:
    print("%s --> %s" % (key, dictionary[key]))

# some_key --> some_value



# iteritems method
dictionary = {
    "some_key": "some_value"
}

for key, value in dictionary.items():
    print("%s --> %s" % (key, value))

# some_key --> some_value
