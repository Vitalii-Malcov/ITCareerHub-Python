""" 09 Звёздочки вместо чисел

Напишите программу, которая заменяет все цифры в строке на звёздочки *.

Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

text = "My number is 123-456-789"

print("Строка:", text)

result = ""

for ch in text:
    if ch.isdigit():
        result += "*"
    else:
        result += ch

print("Результат:", result)
print("Строка:", text)
