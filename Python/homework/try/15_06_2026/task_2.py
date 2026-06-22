""" 02 Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.

ВАЖНО: используйте вывод ошибок
    - и в файл,
    - и на экран.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

"""

"""
02 Логирование ошибок
Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.
ВАЖНО: используйте вывод ошибок
    - и в файл,
    - и на экран.
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s")

file_handler = logging.FileHandler("errors.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def safe_division():
    while True:
        try:
            dividend = input("Введите делимое: ")
            divisor = input("Введите делитель: ")

            a = float(dividend)
            b = float(divisor)
            result = a / b

            print(f"Результат: {result}")
            return True

        except ValueError as e:
            logger.error(f"Ошибка: Введено некорректное число: {e}")
            return False

        except ZeroDivisionError as e:
            logger.error(f"Ошибка: Деление на ноль невозможно: {e}")
            return False

        except TypeError as e:
            logger.error(f"Ошибка: Неподдерживаемый тип данных: {e}")
            return False

safe_division()



