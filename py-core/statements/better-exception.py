def print_each_item(items):

    # check whether items is an Iterable
    try:
        iter(items)
    except TypeError as e:
        raise (
            TypeError(
                f"'items' should be iterable but is of type: {type(items)}")
            .with_traceback(e.__traceback__)
        )

    # if items is iterable, check whether it contains items
    else:
        if items:
            for item in items:
                print(item)

        # if items doesn't contain any items, raise a ValueError
        else:
            raise ValueError("'items' should not be empty")
