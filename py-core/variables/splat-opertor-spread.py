eatables = {
    'mango': '1$',
    'banana': '0.5$'
}

drinks = {
    'water': '0.3$',
    'wine': {
        'white': '2$',
        'red': '1.5$'
    }
}

keys = {
    *eatables,
    *drinks
}

menu = {
    **eatables,
    **drinks
}

print(keys)
print(menu)

# Output: {'wine', 'mango', 'banana', 'water'}
# Output: {'mango': '1$', 'banana': '0.5$', 'water': '0.3$', 'wine': {'white': '2$', 'red': '1.5$'}}
