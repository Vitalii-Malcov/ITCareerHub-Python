""" 01 Повторения букв

Реализуйте функцию, которая
- принимает текст
- и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.

Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""

from collections import Counter


def char_count(text):
    return dict(Counter(c for c in text.lower() if c.isalpha()))


def char_count_1(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result


def char_count_2(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

text = "Programming is fun!"
sample = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}

functions = [char_count, char_count_1, char_count_2]
for func in functions:
    result = func(text)
    print(f"{result}\n{result == sample}\n")

