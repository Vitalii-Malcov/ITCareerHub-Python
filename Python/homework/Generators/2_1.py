""" 02 Генератор уникальных элементов

Создайте генератор, который
- принимает список элементов и выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке

Входные данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

Пример вывода:
3
1
2
4
5
6
7
8

"""
from typing import Generator, Any


def generator_unique_1(items: list[Any]) -> Generator[Any, None, None]:
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def generator_unique_2(items: list[Any]) -> Generator[Any, None, None]:
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
            yield item


def generator_unique_3(items: list[Any]) -> Generator[Any, None, None]:
    def helper(rest, seen):
        if not rest:
            return
        head, *tail = rest
        if head not in seen:
            yield head
            yield from helper(tail, seen | {head})
        else:
            yield from helper(tail, seen)
    yield from helper(items, frozenset())


def generator_unique_4(items: list[Any]) -> Generator[Any, None, None]:
    for i, item in enumerate(items):
        if item not in items[:i]:
            yield item


def generator_unique_5(items: list[Any]) -> Generator[Any, None, None]:
    yield from dict.fromkeys(items)

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


functions = [
    generator_unique_1,
    generator_unique_2,
    generator_unique_3,
    generator_unique_4,
    generator_unique_5,
]

for func in functions:
    print(f"{func.__name__}: {list(func(data))}")
