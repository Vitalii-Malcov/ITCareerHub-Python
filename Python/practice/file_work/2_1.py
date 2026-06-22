"""02 Удаление пустых строк

Напишите программу, которая
- удаляет пустые строки из указанного пользователем файла
- и записывает результат в новый файл.

Имя нового файла формируется автоматически по шаблону <oldname>_cleaned.txt.

Если указанный файл не существует, программа должна вывести ошибку.

Используйте файл tasks.txt.

Пример ввода:
Введите имя файла: tasks.txt

Пример вывода:
Пустые строки удалены, сохранено в tasks_cleaned.txt.
"""

def remove_empty_lines(filename: str) -> None:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            non_empty_lines = [line for line in lines if line.strip()]
            new_filename = f"{filename.rsplit('.', 1)[0]}_cleaned.txt"
            with open(new_filename, 'w', encoding='utf-8') as new_file:
                new_file.writelines(non_empty_lines)
            print(f'Пустые строки удалены, сохранено в {new_filename}.')
    except FileNotFoundError as e:
        print(f'File not found: {e}')


remove_empty_lines('tasks.txt')


remove_empty_lines('t')

