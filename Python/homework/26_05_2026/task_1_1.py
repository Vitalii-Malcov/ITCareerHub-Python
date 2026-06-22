""" 01 Реверс словаря

Напишите программу, которая
- меняет местами ключи и значения в словаре.
Если значения повторяются, добавьте их в список.

ВАЖНО: обратите внимание, что ключи становятся элементами списка,
       даже если значение ключа уникально!

Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}
Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
"""


data = {"a": 1, "b": 2, "c": 1, "d": 3}

inverted_dict = {}
for key, value in data.items():
    if value not in inverted_dict:
        inverted_dict[value] = [key]
    else:
        inverted_dict[value].append(key)
print(f"Перевернутый словарь: {inverted_dict}")


inverted_dict = {
    value: [key for key, val in data.items() if val == value]
    for value in set(data.values())
}
print(f"Перевернутый словарь: {inverted_dict}")


inverted = {}
for key, value in data.items():
    inverted.setdefault(value, []).append(key)
print(f"Перевернутый словарь: {inverted_dict}")


inverted = {}
[inverted.setdefault(value, []).append(key) for key, value in data.items()]
print(f"Перевернутый словарь: {inverted_dict}")


from collections import defaultdict
inverted = defaultdict(list)
for key, value in data.items():
    inverted[value].append(key)
print(f"Перевернутый словарь: {dict(inverted)}")
