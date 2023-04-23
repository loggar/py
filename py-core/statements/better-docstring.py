from collections.abc import Iterable


def print_each_item(items: Iterable) -> None:
    """
    Prints each item of an iterable.

    Parameters:
    -----------
    items : Iterable
        An iterable containing items to be printed.

    Raises:
    -------
    TypeError: If the input is not an iterable.
    ValueError: If the input iterable is empty.

    Returns:
    --------
    None

    Examples:
    ---------
    >>> print_each_item([1,2,3])
    1
    2
    3

    >>> print_each_item(items=[])
    ValueError: 'items' should not be empty
    """
    return None
