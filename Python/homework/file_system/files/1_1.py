""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""

def find_keyword(filename: str, keyword: str) -> None:
    # --- Защита от некорректного ввода (мышление разработчика) ---
    if not isinstance(filename, str) or not isinstance(keyword, str):
        print("Ошибка: имя файла и ключевое слово должны быть строками.")
        return
    if not filename or not keyword:           # пустая строка или ""
        print("Ошибка: имя файла и ключевое слово не должны быть пустыми.")
        return

    # --- Читаем файл построчно: экономно по памяти даже на больших логах ---
    try:
        with open(filename, "r", encoding="utf-8") as src:
            # В список попадают только строки, где встречается keyword
            matched = [line for line in src if keyword.lower() in line.lower()]
    except FileNotFoundError as e:
        # Файла нет — печатаем стандартное сообщение и выходим
        print(f"File not found: {e}")
        return

    # --- Совпадений нет → новый файл НЕ создаём (как требует условие) ---
    if not matched:
        print(f"Совпадения для '{keyword}' не найдены. Файл не создан.")
        return

    # --- Формируем имя <keyword>_<filename> и записываем найденные строки ---
    new_filename = f"{keyword}_{filename}"
    with open(new_filename, "w", encoding="utf-8") as dst:
        dst.writelines(matched)           # writelines не добавляет \n — строки уже с переносами

    print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")


find_keyword('system_log.txt', 'error')


