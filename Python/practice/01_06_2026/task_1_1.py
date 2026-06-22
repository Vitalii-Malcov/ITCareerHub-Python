""" 01 Популярные слова
Реализуйте функцию, которая принимает любое количество строк с текстом.
Функция должна возвращать подсчет самых популярных слов в количестве, переданном в функцию. Программа должна игнорировать регистр слов. Выведите 5 самых популярных слов и их количество.
Данные:
text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
Пример вывода:
5 самых популярных слов:
	words: 3
	text: 3
	with: 2
	sample: 2
	is: 2
"""

from collections import Counter


def popular_words(count, *texts):
    all_text = ' '.join(texts).lower().replace('.','' )
    words = all_text.split()
    counter = Counter(words)
    print(f' 5 самых популярных слов: ')

    for word, qty in counter.most_common(count):
        print(f'\t{word}: {qty}' )



text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."

popular_words(5, text1, text2, text3)
# 5 самых популярных слов:
# 	text: 3
# 	words: 3
# 	is: 2
# 	sample: 2
# 	with: 2
