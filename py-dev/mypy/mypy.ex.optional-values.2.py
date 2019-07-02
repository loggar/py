from typing import Dict


def doubleget(d: Dict[str, int], k) -> int:
    if k in d:
        return d[k] * 2
    else:
        return None


menu: Dict[str, int] = {'coffee': 5, 'sandwich': 7, 'soup': 8}
print(doubleget(menu, 'sandwich'))
print(doubleget(menu, 'elephant'))

# mypy.ex.optional-values.2.py:8: error: Incompatible return value type (got "None", expected "int")
