""" 07 Кодирование строки

Напишите программу, которая
- принимает строку
- и кодирует её с помощью следующего правила:
    - каждая последовательность одинаковых символов заменяется на:
        - символ
        - и количество его повторений.

Например, строка aaaabbc превращается в a4b2c1.

Пример вывода:
Исходная строка: aaaabbc
Закодированная строка: a4b2c1
"""

text = "aaaabbc"

print("Исходная строка:", text)

result = ""
current = text[0]
count = 1

for ch in text[1:]:
    if ch == current:
        count += 1
    else:
        result += current + str(count)
        current = ch
        count = 1

result += current + str(count)
print(result)

