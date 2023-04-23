import logging
from collections.abc import Iterable

logger = logging.getLogger(__name__)


def print_each_item(items: Iterable) -> None:
    """
    <docstring>
    """

    logger.debug(
        f"Printing each item of an object that contains {len(items)} items."
    )

    # check whether items is iterable
    try:
        iter(items)
    except TypeError as e:
        error_msg = f"'items' should be iterable but is of type: {type(items)}"
        logger.error(error_msg)
        raise TypeError(error_msg).with_traceback(e.__traceback__)

    # if items is iterable, check whether it contains items
    else:
        if items:
            for item in items:
                print(item)

        # if items doesn't contain any items, raise a ValueError
        else:
            error_msg = "'items' should not be empty"
            logger.error(error_msg)
            raise ValueError(error_msg)

    return None
