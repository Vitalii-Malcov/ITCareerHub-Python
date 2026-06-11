""" 1. Аннотации для функций

Для каждой из функций, выбранных для решения,
добавьте аннотации типов принимаемых и возвращаемых значений функции.

1.1. Фильтрация чётных с функцией

1.) Напишите УНИВЕРСАЛЬНУЮ функцию-предикат, которая
- проверяет чётный ли переданный элемент.

2.) Также напишите функцию, которая принимает функцию-предикат и список чисел.
- Она должна возвращать новый список, содержащий только элементы,
    для которых предикат возвращает True.

Данные:
nums = [1, 2, 3, 4, 5, 6]
Пример вывода:
[2, 4, 6]
"""

from typing import Callable

def is_even(num: int) -> bool:
    return num % 2 == 0


def filter_by_predicate(predicate:Callable[[int], bool], numbers: list[int]) -> list[int]:
    return [number for number in numbers if predicate(number)]



nums = [1, 2, 3, 4, 5, 6]
sample = [2, 4, 6]

result = filter_by_predicate(is_even, nums)
print(result)            # [2, 4, 6]
print(result == sample)  # True
