""" 03 Проверка знака числа

Напишите функцию, которая
- принимает число
- и возвращает, является ли оно
    - положительным,
    - отрицательным
    - или нулём.


Пример вывода:

# Пример использования:
print(check_number(-5)) # Число отрицательное
print(check_number(0))  # Число равно нулю
print(check_number(5))  # Число положительное

"""
def check_number(num):
    if num > 0:
        return "Число положительное"
    elif num < 0:
        return "Число отрицательное"
    else:
        return "Число равно нулю"

print(check_number(-5))
print(check_number(0))
print(check_number(5))
