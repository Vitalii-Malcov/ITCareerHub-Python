""" 03 Объединение словарей

Напишите функцию, которая
- принимает любое количество словарей
- и объединяет их в один.

Если ключи повторяются, используется значение из последнего словаря.

Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
"""

def merge_dicts_1(*dicts):
    """Объединяет любое количество словарей в один. При совпадении ключей побеждает последний."""
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = value
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
# print(merge_dicts_1(dict1, dict2, dict3))



def merge_dicts_2(*dicts):
    """Объединяет любое количество словарей в один. При совпадении ключей побеждает последний."""
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = {"d": 5}

# print(merge_dicts_2(dict1, dict2, dict3))
from timeit import timeit

print(timeit(merge_dicts_1), range(1_000_000))
print(timeit(merge_dicts_2), range(1_000_000))
