""" 10 Развернуть слова

Напишите программу, которая
- делает реверс каждого слово в строке,
- сохраняя при этом порядок слов.
(т.е. реверсирует слова, а не текст)

Пример вывода:
Строка: Python is fun
Результат: nohtyP si nuf
"""

text = "Python is fun"

print("Строка:", text)

result = []

for word in text.split():
    result += word[::-1] + " "

print("Результат:", ' '.join(result))
print("Строка:", text)
