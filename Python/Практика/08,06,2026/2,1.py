""" 2.1. Фильтрация списка строк

Отфильтруйте в новый список только слова, длина которых больше трех символов.
Реализуйте в виде функции.

Данные:
words = ["hi", "Hello", "a", "python", "Ok"]

Пример вывода:
['Hello', 'python']
"""


def filter_words(words: list[str]) -> list[str]:
    return [word for word in words if len(word) > 3]


words = ["hi", "Hello", "a", "python", "Ok"]
sample = ['Hello', 'python']

result = filter_words(words)

print(result)            # ['Hello', 'python']
print(result == sample)  # True

