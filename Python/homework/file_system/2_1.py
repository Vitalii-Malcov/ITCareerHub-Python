""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys


import os
import sys


def find_files_with_extension(directory, extension):
    """Рекурсивно ищет файлы с заданным расширением."""

    found_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    return found_files


if len(sys.argv) < 3:
    print("Ошибка: нужно указать путь к папке и расширение файла.")
    print("Пример запуска: python 2_1.py C:\\Users\\Vitalii\\Documents .log")

else:
    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.exists(directory):
        print("Ошибка: такой путь не существует.")

    elif not os.path.isdir(directory):
        print("Ошибка: указанный путь не является папкой.")

    else:
        files_to_delete = find_files_with_extension(directory, extension)

        if not files_to_delete:
            print(f"Файлы с расширением '{extension}' не найдены.")

        else:
            print(f"Найдены файлы с расширением '{extension}':")

            for file in files_to_delete:
                print(f"- {file}")

            answer = input("Вы хотите удалить эти файлы? (y/n): ")

            if answer.lower() == "y":
                for file in files_to_delete:
                    os.remove(file)

                print("Удаление завершено.")

            else:
                print("Удаление отменено.")

# 
# import sys
# from pathlib import Path
#
#
# def find_files(directory: Path, extension: str) -> list[Path]:
#     """Рекурсивно находит файлы с заданным расширением."""
#     return list(directory.rglob(f"*{extension}"))
#
#
# def delete_files(files: list[Path]) -> None:
#     """Удаляет файлы, не падая на ошибке отдельного файла."""
#     deleted = 0
#     for file in files:
#         try:
#             file.unlink()
#             deleted += 1
#         except OSError as e:
#             print(f"Не удалось удалить {file}: {e}")
#     print(f"Удаление завершено. Удалено: {deleted} из {len(files)}.")
#
#
# def main() -> None:
#     if len(sys.argv) < 3:
#         sys.exit("Использование: python script.py <путь> <расширение>\n"
#                  "Пример:        python script.py C:\\Users\\Vitalii\\Documents .log")
#
#     directory = Path(sys.argv[1])
#     extension = sys.argv[2]
#     if not extension.startswith("."):      # 'log' → '.log', чтобы не поймать 'catalog'
#         extension = "." + extension
#
#     if not directory.is_dir():             # False и если пути нет, и если это не папка
#         sys.exit(f"Ошибка: '{directory}' не существует или не является папкой.")
#
#     files = find_files(directory, extension)
#     if not files:
#         print(f"Файлы с расширением '{extension}' не найдены.")
#         return
#
#     print(f"Найдены файлы с расширением '{extension}':")
#     for file in files:
#         print(f"- {file}")
#
#     if input("Вы хотите удалить эти файлы? (y/n): ").strip().lower() in ("y", "yes"):
#         delete_files(files)
#     else:
#         print("Удаление отменено.")
#
#
# if __name__ == "__main__":
#     main()
