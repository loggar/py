def multiplier_factory(factor):
    return lambda x: x*factor


doubler = multiplier_factory(2)
print(doubler(4))

# Output: 8
