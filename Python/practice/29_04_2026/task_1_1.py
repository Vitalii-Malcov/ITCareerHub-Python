""" 01 Счётчик слов

Напишите программу, которая
- обрабатывает строку и выводит её,
    - добавив к каждому слову его порядковый номер,
    - выравнивая текст по левому краю с длиной в 15 символов.
    - Слова выводите с большой буквы.

Пример вывода:
Введите строку: Hello world Python is great
1: |Hello          |
2: |World          |
3: |Python         |
4: |Is             |
5: |Great          |
"""

text = "Hello world Python is great"
words = text.split()

index = 1

for word in words:
    word = word.capitalize()
    print(str(index) + ": |" + word.ljust(15) + "|")
    index += 1
