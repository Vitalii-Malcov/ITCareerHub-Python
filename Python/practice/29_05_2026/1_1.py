""" 01 Конвертер температуры

Напишите функцию convert_temperature(), которая
- конвертирует температуру из градусов Цельсия в Фаренгейты
- и наоборот.

Формулы для конвертации температур:
Из градусов Цельсия в Фаренгейты:
F=C×95+32F = C \times \frac{9}{5} + 32

Из градусов Фаренгейта в Цельсия: C=(F−32)×59C = (F - 32) \times \frac{5}{9}

Пример вывода:
print(convert_temperature(100, "C"))  # 100C = 212.0F
print(convert_temperature(100, "F"))  # 100F = 37.8C
print(convert_temperature(100, "K"))  # ОШИБКА! Шкала должна быть 'C' или 'F'.
"""
from unittest import result


def convert_temperature(temp, scale="C"):
    if scale == 'C':
        result = temp * 9 / 5 + 32
        return f"{temp}C = {result:.1f}F"
    elif scale == 'F':
        result = (temp - 32) * 5 / 9
        return f"{temp}F = {result:.1f}C"
    else:
        return "ОШИБКА! Шкала должна быть 'C' или 'F'."


print(convert_temperature(100, "C"))  # 100C = 212.0F
print(convert_temperature(100, "F"))  # 100F = 37.8C
print(convert_temperature(100, "K"))  # ОШИБКА! Шкала должна быть 'C' или 'F'.
