from typing import Dict, Optional


def doubleget(d: Dict[str, int], k) -> Optional[int]:
    if k in d:
        return d[k] * 2
    else:
        return None

# By annotating the function's return type with Optional[int], this is saying that if something is returned, it will be an integer. But, it's also okay to return None.
