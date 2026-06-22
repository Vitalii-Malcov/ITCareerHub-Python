""" 7*. Поиск максимального элемента

Отсортируйте слова в списке исходя из суммы порядковых номеров всех символов в слове.
К примеру "kiwi" = ord("k") + ord("i") + ord("w") + ord("i") = 107 + 105 + 119 + 105 = 436.
Попробуйте решить в одну строку с помощью lambda и функций высшего порядка.

Данные:
words = ["banana", "kiwi", "grapefruit", "apple"]
Пример вывода:
['kiwi', 'apple', 'banana', 'grapefruit']



СПОСОБ РЕШЕНИЯ

Попробуйте решить поэтапно:

1. Найдите сумму порядковых номеров всех символов в одном слове.

2 Напишите функцию, которая сортирует слова по длине.

3 Замените сортировку по длине на сортировку по сумме порядковых номеров"""


def word_sum(word):
    return sum(map(ord, word))


def sort_words_by_ord_sum(words):
    return sorted(words, key=word_sum)


words = ["banana", "kiwi", "grapefruit", "apple"]

result = sort_words_by_ord_sum(words)

print(result)
