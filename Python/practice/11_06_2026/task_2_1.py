""" 02 Функция mdc (my deepcopy)

Реализуйте аналог deepcopy() с помощью рекурсии.
Не забудьте проверить, чтобы изменения в копии не затронули оригинал.

Данные:
original_data = [
    [1, 2, 3],                 # Вложенный список
    (4, [5, 6], {7, 8}),       # Тюпл с вложенными структурами
    {"a": 9, "b": [10, 11]},   # Словарь со списком
    "Hello",                   # Строка
    [12, (13, 14)],            # Список с тюплом
    15.5,                      # Число с плавающей точкой
    5                          # Целое число
]
Пример вывода:
Исходный: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
Копия:    [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]

"""

# def mdc(original_data):
#     # Если объект — список
#     if isinstance(original_data, list):
#         new_list = []
#         for item in original_data:
#             new_list.append(mdc(item))
#         return new_list
#     # Если объект — кортеж / tuple
#     if isinstance(original_data, tuple):
#         new_tuple = ()
#         for item in original_data:
#             new_tuple = new_tuple + (mdc(item),)
#         return new_tuple
#     # Если объект — множество / set
#     if isinstance(original_data, set):
#         new_set = set()
#         for item in original_data:
#             new_set.add(item)  # Элементы множества должны быть hashable
#         return new_set
#     # Если объект — словарь / dict
#     if isinstance(original_data, dict):
#         new_dict = {}
#         for key, value in original_data.items():
#             new_dict[key] = mdc(value)  # Ключи должны быть hashable
#         return new_dict
#     # Примитивы (int, float, str, bool и т.д.) — возвращаем как есть
#     return original_data


def mdc(original_data):
    if isinstance(original_data, list):
        return [mdc(item) for item in original_data]
    if isinstance(original_data, tuple):
        return tuple(mdc(item) for item in original_data)
    if isinstance(original_data, set):
        return original_data.copy()
    if isinstance(original_data, dict):
        return {k: mdc(v) for k, v in original_data.items()}
    return original_data

od = [
    [1, 2, 3],
    (4, [0, 6], {8, 7}),
    {'a': 9, 'b': [10, 11]},
    'Hello',
    [12, (13, 14)],
    15.5,
    5
]

od_copy = mdc(od)
print(od_copy)
print(od == od_copy)  # True

# Меняем исходный список
od[0][1] = 5
print(od)
print(od_copy)
print(od == od_copy)  # False


