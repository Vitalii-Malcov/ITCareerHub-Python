""" 01. Одно слово

Напишите программу, которая
- обрабатывает список из строк
- и удаляет все строки, содержащие более одного слова,
- а также преобразует оставшиеся строки к нижнему регистру.

ВАЖНО: НЕ создать новый список, а УДАЛИТЬ лишние элементы из существующего!

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple", "Test String"]

# for i in range(len(text_list))[::-1]: # или for i in range(len(text_list)-1, -1, -1):
#     if len(text_list[i].split()) > 1:
#         del text_list[i]
#     else:
#         text_list[i] = text_list[i].lower()
# print(text_list)


# Вариант 2 ................................................................................

# i = 0
#
# while i < len(text_list):
#     word = text_list[i]
#     if " " in word:
#         text_list.pop(i)
#     else:
#         text_list[i] = word.lower()
#         i += 1
# print(text_list)


# И пайтоник Вариант на мой взгляд...........................................................
text_list[:] = [
    word.lower()
    for word in text_list
    if " " not in word
]
print(text_list)

