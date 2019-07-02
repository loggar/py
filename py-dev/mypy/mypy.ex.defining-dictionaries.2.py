from typing import Dict

menu: Dict[str, int] = {'coffee': 5, 'sandwich': 7, 'soup': 8}
menu[5] = 'muffin'

# mypy.ex.defining-dictionaries.2.py:4: error: Invalid index type "int" for "Dict[str, int]"; expected type "str"
# mypy.ex.defining-dictionaries.2.py:4: error: Incompatible types in assignment (expression has type "str", target has type "int")
