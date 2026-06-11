""" 03 Самое длинное слово
Дано предложение.
Найдите самое длинное слово
и выведите это слово с его длиной.

Данные:
sentence = "Programming in Python is both fun and educational"

Пример вывода:
Самое длинное слово: Programming
Длина слова: 11
"""

sentence = "Programming in Python is both fun and educational"
words = sentence.split()

longest = max(words, key=len)

# for word in words:
#     if len(word) > len(longest):
#         longest = word

print(f"Самое длинное слово: {longest}")
print(f"Длина слова: {len(longest)}")
