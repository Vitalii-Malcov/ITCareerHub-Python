""" 01 Объединение данных в строку

Напишите функцию, которая
- принимает список любых данных (строки, числа, списки, словари)
- и возвращает их строковое представление, объединённое через " | ".
  (т.е. объединяет результат в одну строку)

Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.


Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
"""

from typing import Any


def join_data(data: list[Any]) -> str:
    """Объединяет элементы списка в одну строку через ' | '."""
    return " | ".join(map(str, data))


def join_data_2(data: list[Any]) -> str:
    parts = []
    for item in data:
        parts.append(str(item))
    return " | ".join(parts)

def join_data_3(data: list[Any]) -> str:
    return " | ".join([str(item) for item in data])

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

print(join_data(data))
print(join_data_2(data))
print(join_data_3(data))
