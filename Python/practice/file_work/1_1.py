"""01 Подсчёт частоты слов в файле

Напишите программу, которая
- подсчитывает, сколько раз каждое слово встречается в файле (не учитывая регистр).

Программа запрашивает имя файла и количество популярных слов для вывода.

Если указанный файл не существует, программа должна вывести ошибку.

Используйте файл text.txt.

Пример ввода:
Введите имя файла: text.txt
Введите количество популярных слов: 3

Популярные слова:
the: 27
of: 21
lorem: 17

"""
from collections import Counter


def count_words(file_name: str, num_words: int) -> None:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = text.split()
            word_counts = Counter(words)
            most_common = word_counts.most_common(num_words)
            print('Популярные слова:')
            for word, count in most_common:
                print(f'{word}: {count}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')


count_words('text.txt', 3)


