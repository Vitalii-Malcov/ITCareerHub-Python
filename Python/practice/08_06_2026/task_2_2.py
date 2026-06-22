"""
2.2. Фильтрация списка строк по длине

Доработайте функцию так, чтобы можно было передавать значение минимальной длины слов, которые нужно оставить.
words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 2

Пример вывода:
['hi', 'Hello', 'python', 'Ok']
"""


def filter_words(words: list[str], min_len: int) -> list[str]:
    return [word for word in words if len(word) >= min_len]

words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 2

sample = ['hi', 'Hello', 'python', 'Ok']

result = filter_words(words, min_len)
print(result)            # ['hi', 'Hello', 'python', 'Ok']
print(result == sample)  # True
