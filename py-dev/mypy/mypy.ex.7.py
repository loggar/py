from typing import Iterable, Union


def mysum(numbers: Iterable[Union[int, float]]) -> Union[int, float]:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10.1, 20.2, 30.3, 40, 50)))
