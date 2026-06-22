""" 02 Сумма вложенных чисел

Напишите функцию, которая
- принимает список словарей, где каждый словарь содержит
    - имя пользователя
    - и список баллов.
- Функция должна вернуть сумму всех чисел.
- Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:
Итоговый балл: 156
"""

from typing import Any
from functools import reduce

def total_scores(data: list[dict[str, Any]]) -> int:
    """Считает сумму всех баллов из списка пользователей."""
    return sum(sum(user["scores"]) for user in data)


def total_scores_2(data: list[dict[str, Any]]) -> int:
    return reduce(lambda acc, user: acc + sum(user["scores"]), data, 0)


def total_scores_3(data: list[dict[str, Any]]) -> int:
    return sum(map(lambda user: sum(user["scores"]), data))


def total_scores_4(data: list[dict[str, Any]]) -> int:
    total = 0
    for user in data:
        for score in user["scores"]:
            total += score
    return total


data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]},
]

print(f"Итоговый балл: {total_scores(data)}")
print(f"Итоговый балл: {total_scores_2(data)}")
print(f"Итоговый балл: {total_scores_3(data)}")
print(f"Итоговый балл: {total_scores_4(data)}")


