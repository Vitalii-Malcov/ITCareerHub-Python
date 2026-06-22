"""01 Сумма чисел списка

Напишите рекурсивную функцию, которая
- вычисляет сумму всех чисел в списке.

Функция должна проверять:
- Аргумент должен быть списком.
- Все элементы списка должны быть числами.

Если данные не валидны необходимо выбрасывать исключение.
При вызове функции обработайте возможное исключение.

Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
15
"""

def recursive_sum(lst):
    if not lst:
        return 0
    if not isinstance(lst, list):
        raise TypeError(f'Ожидался список, получено {type(lst)}')
    for item in lst:
        if not isinstance(item, int):
            raise ValueError (f'Все элементы должны быть числами, найдено {type(item)}')

    return lst[0] + recursive_sum(lst[1:])


numbers = [1, 2, 3, 4, 5,]

try:
    result = recursive_sum(numbers)
    print(result)
except (TypeError, ValueError) as e:
    print(f"Ошибка: {e}")


# recursive_sum([1, 2, 3, 4, 5])
# 1 + recursive_sum([2, 3, 4, 5])
# 1 + 2 + recursive_sum([3, 4, 5])
# 1 + 2 + 3 + recursive_sum([4, 5])
# 1 + 2 + 3 + 4 + recursive_sum([5])
# 1 + 2 + 3 + 4 + 5 + recursive_sum([])
# 1 + 2 + 3 + 4 + 5 + 0 = 15
