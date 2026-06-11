""" 2.3. Фильтрация списка строк по критерию

Доработайте функцию так, чтобы можно было передавать критерии отбора слов, которые нужно оставить.
(то есть аргументом должен стать callable-объект)
Например:
- слова, начинаются с заглавной буквы
- слова из одного символа
- слова начинаются и заканчиваются одной буквой, независимо от регистра

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
Пример вывода:
['Hello', 'Ok', 'Radar']
['a']
['a', 'Radar']
"""
from typing import Callable

def filter_words(words: list[str], criterion: Callable[[str], bool]) -> list[str]:
    return [word for word in words if criterion(word)]

def start_words(word: str) -> bool:
    return word[0].isupper()

def is_one(word: str) -> bool:
    return len(word) == 1

def start_end(word: str) -> bool:
    return word[0].lower() == word[-1].lower()

words = ["hi", "Hello", "a", "python", "Ok", "Radar"]



result1 = filter_words(words, start_words)
result2 = filter_words(words, is_one)
result3 = filter_words(words,start_end)

print(result1)            # ['Hello', 'Ok', 'Radar']
print(result2)
print(result3)# ['a']
# print(result3)            # ['a', 'Radar']
