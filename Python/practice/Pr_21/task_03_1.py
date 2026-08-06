""" 03. Меню книжного магазина

3.1. Загрузка книг из файла

Добавьте пункт меню, который позволяет загрузить список книг из файла.
Каждая строка файла содержит: название, автор, цена, количество;
Если книга с таким названием и автором уже есть — обновляется количество;
Если такой книги нет — создаётся новая запись;
После завершения загрузки выводится количество обработанных книг.

Пример файла:
1984,George Orwell,8.99,5
Brave New World,Aldous Huxley,9.50,3
Пример вывода:
2 books loaded.
"""


def load_books_from_file(filename, connection, db_name):
    added = 0  # подсчитываем кол-во добавленных книг
    with open(filename, "r", encoding="utf-8") as file:   # открываем файл
        with connection.cursor() as cursor:
            for i, line in enumerate(file):
                line = line.strip()
                if not line:
                    continue

                if i == 0 and line.lower().startswith("title"):  # пропускаем заголовок
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                title, author, price_str, stock_str = (p.strip() for p in parts)

                try:
                    price = float(price_str)
                    stock = float(stock_str)
                except ValueError:
                    continue

                cursor.execute(
                    "SELECT id, stock FROM books WHERE title = %s AND author = %s",
                    (title, author)
                )

                existing = cursor.fetchone()

                if existing:
                    book_id, current_stock = existing
                    cursor.execute(
                        "UPDATE books SET stock = %s WHERE id = %s",
                        (current_stock + stock, book_id)
                    )
                else:
                    cursor.execute(
                        "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)",
                        (title, author, price, stock)
                    )
                added += 1

            connection.commit()


    print(f"{added} books loaded.")

# Database '010825_bookstore_BAR' created or already exists.
# Tables in '010825_bookstore_BAR':
# - books
# - users
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 1
#
# --- Bookstore Menu ---
# 1. Load books from file
# Enter file name: books.csv
# 12 books loaded.
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
