from typing import Dict

menu: Dict[str, int] = {'coffee': 5, 'sandwich': 7, 'soup': 8.5}

# mypy.ex.defining-dictionaries.3.py:3: error: Dict entry 2 has incompatible type "str": "float"; expected "str": "int"