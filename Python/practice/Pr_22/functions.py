

from queries import text_user_menu
from task_04_1 import view_available_books
from task_04_2 import search_books_by_title
from task_04_3 import purchase_book
from task_07 import show_popular_queries



# ---------------------------------------------------------------------------
# 3.1. Загрузка книг из файла
# ---------------------------------------------------------------------------
def load_books_from_file(filename, connection, db_name):
    """
    Каждая строка файла: title, author, price, stock.
    Если книга (title + author) уже есть — обновляется stock (суммируется).
    Если книги нет — создаётся новая запись.
    """
    added = 0
    with open(filename, "r", encoding="utf-8") as file:
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
                    (title, author),
                )
                existing = cursor.fetchone()

                if existing:
                    book_id, current_stock = existing
                    cursor.execute(
                        "UPDATE books SET stock = %s WHERE id = %s",
                        (current_stock + stock, book_id),
                    )
                else:
                    cursor.execute(
                        "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)",
                        (title, author, price, stock),
                    )
                added += 1

            connection.commit()

    print(f"{added} books loaded.")


# ---------------------------------------------------------------------------
# 3.2. Регистрация клиента
# ---------------------------------------------------------------------------
def register_user(connection, db_name):
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance.")
        return

    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        if cursor.fetchone() is not None:
            print("Username already exists.")
            return

        cursor.execute(
            "INSERT INTO users (username, password, balance) VALUES (%s, %s, %s)",
            (username, password, balance),
        )
        connection.commit()

    print("Registration successful.")


# ---------------------------------------------------------------------------
# 3.3. Вход в аккаунт + подменю клиента
# ---------------------------------------------------------------------------
def try_login(connection, db_name):
    username = input("Enter username: ")
    password = input("Enter password: ")

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM users WHERE username = %s AND password = %s",
            (username, password),
        )
        row = cursor.fetchone()

    if row:
        print("Login successful.")
        return row[0]  # user_id

    print("Invalid username or password.")
    return None


def user_menu(connection, user_id, db_name, searches_collection):
    while True:
        choice = input(text_user_menu.format(user_id=user_id))

        # Единая if/elif-цепочка (в исходнике elif/else были привязаны
        # только к последнему if, из-за чего меню работало некорректно)
        if choice == "1":
            view_available_books(connection, user_id, db_name)
        elif choice == "2":
            search_books_by_title(connection, user_id, db_name, searches_collection)
        elif choice == "3":
            purchase_book(connection, user_id, db_name)
        elif choice == "4":
            show_popular_queries(searches_collection)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")
