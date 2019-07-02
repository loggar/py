from typing import Dict


def doubleget(d: Dict[str, int], k) -> int:
    return d[k] * 2


menu: Dict[str, int] = {'coffee': 5, 'sandwich': 7, 'soup': 8}
print(doubleget(menu, 'sandwich'))

# This is fine, but what happens if the user passes a key that isn't in the dict?
# This will end up raising a KeyError exception.
# I'd like to do what the dict.get method does—namely return None if the key is unknown.
