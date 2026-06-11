""" 04 Проверка скобок

Напишите программу, которая
- проверяет правильность расстановки круглых скобок в строке.

Пример вывода:
Введите строку: (a+b)*(c-d)
Скобки расставлены правильно? True

Введите строку: (a+b)(*((c-d)
Скобки расставлены правильно? False
"""


string = input("Введите строку: ")

count = 0
correct = True

for char in string:
    if char == '(':
        count += 1
    elif char == ')':
        count -= 1
    if count < 0:
        correct = False
        break

if count != 0:
    correct = False

print("Скобки расставлены правильно?", correct)
