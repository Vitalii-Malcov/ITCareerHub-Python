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
    if not isinstance(filename, str):
        print("Ошибка: имя файла должно быть строкой.")
        return
    if not filename:
        print("Ошибка: имя файла не должно быть пустым.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # Убираем дубликаты, сохраняя порядок dict.fromkeys() запоминает порядок вставки
    # и хранит каждый ключ только один раз дубликаты исчезают сами
    unique = list(dict.fromkeys(lines))

    new_filename = f"unique_{filename}"
    with open(new_filename, "w", encoding="utf-8") as dst:
        dst.writelines(unique)

    print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}.")

remove_duplicates("movies_to_watch.txt")



