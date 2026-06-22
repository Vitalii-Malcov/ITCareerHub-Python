"""02 Фильтрация по символу
Создайте новый список, исключив все строки,
содержащие символ, который введет пользователь.

Данные:
words = ["apple", "cherry", "kiwi", "banana", "orange"]

Пример вывода:
Исключить символ: r
['apple', 'kiwi', 'banana']
"""
from unittest import result

words = ["apple", "cherry", "kiwi", "banana", "orange"]
char = "r"

filtered_words = [word for word in words if char not in word]

print(filtered_words)
