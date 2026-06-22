"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""


import sys
import os

# Проверяем, передал ли пользователь путь
if len(sys.argv) < 2:
    print("Ошибка: укажите путь к директории.")
    print("Пример запуска: python script.py /home/user/documents")
else:
    directory_path = sys.argv[1]

    # Проверяем, существует ли такой путь
    if not os.path.exists(directory_path):
        print("Ошибка: такой путь не существует.")

    # Проверяем, что это именно папка
    elif not os.path.isdir(directory_path):
        print("Ошибка: указанный путь не является директорией.")

    else:
        folders = []
        files = []

        # Получаем список содержимого директории
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)

            if os.path.isdir(full_path):
                folders.append(item)

            elif os.path.isfile(full_path):
                files.append(item)

        print(f"Содержимое директории '{directory_path}':")

        print("Папки:")
        for folder in folders:
            print(f"- {folder}")

        print("Файлы:")
        for file in files:
            print(f"- {file}")
