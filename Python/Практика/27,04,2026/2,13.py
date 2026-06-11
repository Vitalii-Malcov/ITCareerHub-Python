""" 13 Все позиции подстроки
Напишите программу, которая
- ищет подстроку в строке
- и выводит все индексы начала вхождения подстроки.

ВАЖНО: программа должна быть регистро-независимой!

Пример вывода:
Строка: Banana bAnana baNAna
Подстрока: ban
Позиция: 0
Позиция: 7
Позиция: 14
"""

text = "Banana bAnana baNAna"
substring = "ban"

print("Строка:", text)
print("Подстрока:", substring)

text_lower = text.lower()
sub_lower = substring.lower()

for i in range(len(text) - len(substring) + 1):
    if text_lower[i:i + len(substring)] == sub_lower:
        print("Позиция:", i)

print("Строка:", text)
print("Подстрока:", substring)
