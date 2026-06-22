""" 07 Создание глобального счётчика

Создайте функцию increment_counter, которая
- использует глобальную переменную counter для подсчёта вызовов этой функции.

Пример вызова:
increment_counter()
increment_counter()
print(counter)

Пример вывода:
Вызовов функции: 2
"""

counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()
print("Вызовов функции:", counter)
