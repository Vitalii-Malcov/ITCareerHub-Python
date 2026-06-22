""" 02 Список уникальных слов

Дан текст. Программа должна:
Разбить текст на слова.
Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
Вывести количество уникальных слов.

Данные:
text = "Python is a great programming language. Python is popular and powerful."

Пример вывода:
Количество уникальных слов: 9
Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']
"""

text = "Python is a great programming language. Python is popular and powerful."

words = text.lower().replace(".", "").split()
uniq = []

for word in words:
    if word not in uniq:
        uniq.append(word)

print(f"Количество уникальных слов: {len(uniq)}")
print("Уникальные слова:", sorted(uniq))
