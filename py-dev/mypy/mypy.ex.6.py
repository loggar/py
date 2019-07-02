from typing import Iterable


def mysum(numbers: Iterable[int]) -> int:
    output = 0
    for one_number in numbers:
        output += one_number
    return output


print(mysum([10, 20, 30, 40, 50]))
print(mysum((10, 20, 30, 40, 50)))
print(mysum([10, 20, 'abc', 'def', 50]))
print(mysum('abcd'))
