""" 4. Сортировка списка по длине

Отсортируйте список слов по длине, используя параметр.

ВАЖНО: Обратите внимание на порядок отсортированных строк в примере:
Использована двух-уровневая сортировка:
 - прямая по длине слова;
 - и обратная по алфавиту.

Данные:
words = ["apple", "banana", "kiwi", "grape"]
print(sort_by_length(words))
Пример вывода:
['kiwi', 'grape', "apple", 'banana']
"""

def sort_by_length_1(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: (len(word), -ord(word[0])))

def sort_by_length(words: list[str]) -> list[str]:
    sorted_words = sorted(words, reverse=True)
    return sorted(sorted_words, key=len)



sample = ['kiwi', 'grape', "apple", 'banana']
words = ["apple", "banana", "kiwi", "grape"]

result = sort_by_length(words)
result1 = sort_by_length_1(words)
print(result)
print(result1)
print(result == sample)
# print(sort_by_length(words))
