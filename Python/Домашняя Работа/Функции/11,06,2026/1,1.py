""" 01 Сумма цифр числа

Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
num = 43197
Пример вывода:
24
"""

def sum_digits_non_tail(num):
    if num == 0:
        return 0
    return num % 10 + sum_digits_non_tail(num // 10)


def sum_digits_tail(num, accumulator=0):
    if num == 0:
        return accumulator
    return sum_digits_tail(num // 10, accumulator + num % 10)


print(sum_digits_tail(43197))       # 24
print(sum_digits_non_tail(43197))   # 24
