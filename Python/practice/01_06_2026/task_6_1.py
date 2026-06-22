""" 06 Группировка слов по длине
Реализуйте функцию, которая группирует слова по их длине в и возвращает словарь с ними.
Данные:
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]

Пример вывода:
Слова по длине:
5: ['apple', 'grape', 'peach']
6: ['banana', 'orange']
4: ['kiwi']
"""

from collections import defaultdict


def group_words_by_length(words):
    result = defaultdict(list)
    for word in words:
        result[len(word)].append(word)
    return dict(result)


words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]
result = group_words_by_length(words)

print("Слова по длине:")
for length, words in result.items():
    print(f"{length}: {words}")
