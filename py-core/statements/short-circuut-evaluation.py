thirsty = True

drink = {
    'type': 'banana split',
    'empty': True,
}


def makeDrink(drink_type):
    return {
        'type': drink_type,
        'empty': False,
    }


drink_from = thirsty and (not drink['empty'] or makeDrink('gin tonic'))

print(drink_from)

# Output: {'type': 'gin tonic', 'empty': False}
