""" 01 Фабрика функций округления

Создайте функцию make_rounder(), которая
 - принимает количество знаков для округления
 - и возвращает другую функцию.

Полученная функция должна принимать число и возвращать его,
округлённое до указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода:
3.14
2.72
10.0
"""


from functools import partial
from typing import Callable


def make_rounder_v1(num_digits: int) -> Callable:
    def rounder(number: float) -> float:
        return round(number, num_digits)
    return rounder


def make_rounder_v2(num_digits: int) -> Callable:
    return lambda number: round(number, num_digits)


def make_rounder_v3(num_digits: int) -> Callable:
    return partial(round, ndigits=num_digits)


def make_rounder_v4(num_digits: int) -> Callable:
    def rounder(number: float, digits: int = num_digits) -> float:
        return round(number, digits)
    return rounder


if __name__ == "__main__":
    for name, factory in [
        ("v1 (closure)", make_rounder_v1),
        ("v2 (lambda)", make_rounder_v2),
        ("v3 (partial)", make_rounder_v3),
        ("v4 (default arg)", make_rounder_v4)]:

        round2 = factory(2)
        round0 = factory(0)
        print(f"--- {name} ---")
        print(round2(3.14159))
        print(round2(2.71828))
        print(round0(9.999))
