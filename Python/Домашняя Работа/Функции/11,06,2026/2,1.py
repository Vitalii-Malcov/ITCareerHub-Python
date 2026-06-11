""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""


def sum_digits_non_tail(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):

            total += sum_digits_non_tail(item)
    return total


def sum_digits_non_tail_2(lst):
    return sum(item if isinstance(item, int) else sum_digits_non_tail(item) for item in lst)


def sum_digits_tail(lst, acc=0):
    if not lst:
        return acc
    head, *tail = lst
    if isinstance(head, int):
        return sum_digits_tail(tail, acc + head)
    elif isinstance(head, list):
        return sum_digits_tail(head + tail, acc)
    else:
        return sum_digits_tail(tail, acc)




nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))       # 28
print(sum_digits_non_tail(nested_numbers))   # 28
print(sum_digits_non_tail_2(nested_numbers)) # 28

# коротко описал таблицу понимания работы функции!!!
# 1. lst = [1, [2, 3], [4, [5, 6]], 7]      acc = 0
# 2. lst = [[2, 3], [4, [5, 6]], 7]         acc = 1
# 3. lst = [2, 3, [4, [5, 6]], 7]           acc = 1
# 4. lst = [3, [4, [5, 6]], 7]              acc = 3
# 5. lst = [[4, [5, 6]], 7]                 acc = 6
# 6. lst = [4, [5, 6], 7]                   acc = 6
# 7. lst = [[5, 6], 7]                      acc = 10
# 8. lst = [5, 6, 7]                        acc = 10
# 9. lst = [6, 7]                           acc = 15
# 10. lst = [7]                             acc = 21
# 11. lst = []                              acc = 28
