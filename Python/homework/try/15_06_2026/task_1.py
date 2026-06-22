""" 01 Деление без ошибок

Напишите функцию, которая
- выполняет деление двух чисел, введенных пользователем,
- и обрабатывает возможные ошибки.

ВАЖНО: Используйте несколько обработок различных ошибок

Примеры вывода:

Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.

Введите делимое: 5
Введите делитель: 0
Ошибка: Деление на ноль невозможно.

Введите делимое: 5
Введите делитель: 2
Результат: 2.5

"""

def safe_division():
    try:
        dividend = input("Введите делимое: ")
        divisor = input("Введите делитель: ")

        a = float(dividend)
        b = float(divisor)
        result = a / b

        print(f"Результат: {result}")
        return True

    except ValueError:
        print("Ошибка: Введено некорректное число.")
        return False

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
        return False

    except TypeError:
        print("Ошибка: Неподдерживаемый тип данных.")
        return False

safe_division()


# def get_float(number):
#     while True:
#         try:
#             return float(input(number))
#         except ValueError:
#             print("Ошибка: Введено некорректное число. Попробуйте снова.\n")
#
# def safe_division():
#     a = get_float("Введите делимое: ")
#     b = get_float("Введите делитель: ")
#
#     if b == 0:
#         print("Ошибка: Деление на ноль невозможно.")
#         return False
#
#     print(f"Результат: {a / b}")
#     return True
#
# safe_division()


# def safe_division():
#     while True:
#         try:
#             a = float(input("Введите делимое: "))
#             b = float(input("Введите делитель: "))
#             result = a / b
#         except (ValueError, ZeroDivisionError) as e:
#             match e:
#                 case ValueError():
#                     print("Ошибка: Введено некорректное число.\n")
#                 case ZeroDivisionError():
#                     print("Ошибка: Деление на ноль невозможно.\n")
#         else:
#             print(f"Результат: {result}")
#             return True
#
# safe_division()


# def is_number(value):
#     return value.replace('.', '', 1).replace('-', '',1).isdigit()
#
# def safe_division():
#     dividend = input("Введите делимое: ")
#     divisor = input("Введите делитель: ")
#
#     if not is_number(dividend) or not is_number(divisor):
#         print("Ошибка: Введено некорректное число.")
#         return False
#
#     a, b = float(dividend), float(divisor)
#
#     if b == 0:
#         print("Ошибка: Деление на ноль невозможно.")
#         return False
#
#     print(f"Результат: {a / b}")
#     return True
#
# safe_division()
