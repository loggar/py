from typing import Dict, Union

menu: Dict[str, Union[int, float]] = {'coffee': 5, 'sandwich': 7, 'soup': 8.5}
menu[5] = 'muffin'

# mypy.ex.defining-dictionaries.4.py:4: error: Invalid index type "int" for "Dict[str, Union[int, float]]"; expected type "str"
# mypy.ex.defining-dictionaries.4.py:4: error: Incompatible types in assignment (expression has type "str", target has type "Union[int, float]")
