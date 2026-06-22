""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""

def remove_duplicates(filename: str) -> None:
    pass



remove_duplicates("movies_to_watch.txt")
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

remove_duplicates("M")
# File not found: [Errno 2] No such file or directory: 'M'
