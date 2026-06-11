""" 02 Фильтрация списка по длине

Создайте функцию filter_strings(), которая
- принимает целое число n
- и любое количество строк (по отдельности, а не как коллекция).

Функция должна возвращать список строк, длина которых больше n.

Данные:
strings = ["apple", "banana", "cherry", "date", "fig"]
n = 5

Пример вывода:
['banana', 'cherry']

"""
def filter_strings(n, *args):
    result = []
    for s in args:
        if len(s) > n:
            result.append(s)
    return result

strings = ["apple", "banana", "cherry", "date", "fig"]
n = 5
print(filter_strings(n, *strings))  # ['banana', 'cherry']
