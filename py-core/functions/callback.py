def take_five(callback):
    callback(5)


take_five(lambda x: print(x*x))

# Output: 25
