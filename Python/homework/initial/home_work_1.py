
import math


# Округление числа до целого по правилам математики
# Использую сдвиг +0.5 для положительных и -0.5 для отрицательных чисел

number = float(input("Введите вещественное число: "))

if number >= 0:
    result = math.floor(number + 0.5)
else:
    result = math.ceil(number - 0.5)

print("Округленное значение:", result)


# Округление числа через разделение на целую и дробную часть
# Проверяю дробную часть и решаю, увеличивать число или нет

number = float(input("Введите число: "))

integer = int(number)
fraction = number - integer

if number >= 0:
    if fraction >= 0.5:
        result = integer + 1
    else:
        result = integer
else:
    if fraction <= -0.5:
        result = integer - 1
    else:
        result = integer

print("Округленное значение:", result)


# Округление числа с использованием модуля (abs)
# Сначала определяю размер дробной части без знака,
# затем решаю, в какую сторону округлять

number = float(input("Введите число: "))

integer = int(number)
fraction = abs(number - integer)

if fraction >= 0.5:
    if number > 0:
        result = integer + 1
    else:
        result = integer - 1
else:
    result = integer

print("Округленное значение:", result)
