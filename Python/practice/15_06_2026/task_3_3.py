""" 03 Глубина вложенности списка

Напишите рекурсивную функцию, которая
- определяет максимальную глубину вложенности списка.

Функция должна проверять:
- Аргумент должен быть списком.
- Вложенные структуры, если они есть, также должны быть списками.
- Если данные не валидны необходимо выбрасывать исключение.

При вызове функции обработайте возможное исключение.

Данные:
nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]

Пример вывода:
Максимальная глубина: 5
"""

nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]


def max_depth(data: list) -> int:
    if not isinstance(data, list):
        raise TypeError(f"Ожидается список, получено: {type(data)}")
    if not data:
        return 1
    max_child = 0

    for item in data:
        if isinstance(item, list):
            child_depth = max_depth(item)
            if child_depth > max_child:
                max_child = child_depth
        elif not isinstance(item, (int, float, str, bool, type(None))):
            raise TypeError(f"Недопустимый тип вложенного элемента: {type(item)}")
    return 1 + max_child


try:
    depth = max_depth(nested_list)
    print(f"Максимальная глубина: {depth}")
except TypeError as e:
    print(f"Ошибка типа данных: {e}")


# recursive_sum([1, 2, 3, 4, 5])
#    1 + recursive_sum([2, 3, 4, 5])
#          2 + recursive_sum([3, 4, 5])
#                  3 + recursive_sum([4, 5])
#                          4 + recursive_sum([5])
#                                  5 + recursive_sum([])
