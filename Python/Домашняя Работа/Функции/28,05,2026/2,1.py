""" 02 Фильтрация чисел по чётности

Напишите функцию filter_type, которая
- принимает первый аргумент ("even" или "odd")
- и произвольное количество чисел,
- возвращая только те, которые соответствуют фильтру.

Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""

def is_even(n):
    """Возвращает True, если число n чётное."""
    return n % 2 == 0

def is_odd(n):
    """Возвращает True, если число n нечётное."""
    return n % 2 != 0

def filter_numbers(filter_type, *numbers):
    """Фильтрует числа по типу: 'even' — чётные, 'odd' — нечётные."""
    result = []
    if filter_type == "even":
        for n in numbers:
            if is_even(n):
                result.append(n)
    elif filter_type == "odd":
        for n in numbers:
            if is_odd(n):
                result.append(n)
    else:
        return "Некорректный фильтр"
    return result

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))


def is_even(n):
    """Возвращает True, если число n чётное."""
    return n % 2 == 0

def is_odd(n):
    """Возвращает True, если число n нечётное."""
    return n % 2 != 0

def filter_numbers(filter_type, *numbers):
    """Фильтрует числа по типу: 'even' — чётные, 'odd' — нечётные."""
    if filter_type == "even":
        return [n for n in numbers if is_even(n)]
    elif filter_type == "odd":
        return [n for n in numbers if is_odd(n)]
    else:
        return "Некорректный фильтр"

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
