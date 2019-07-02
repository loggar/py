menu = {'coffee': 5, 'sandwich': 7, 'soup': 8}
menu[5] = 'muffin'

# mypy.ex.defining-dictionaries.1.py:2: error: Invalid index type "int" for "Dict[str, int]"; expected type "str"
# mypy.ex.defining-dictionaries.1.py:2: error: Incompatible types in assignment (expression has type "str", target has type "int")
