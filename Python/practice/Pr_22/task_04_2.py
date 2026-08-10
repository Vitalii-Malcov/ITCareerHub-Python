""" 4.2. Поиск книги по названию
Добавьте в дополнительное меню возможность искать книги по названию (или его части).
Пользователь вводит фрагмент названия;
Выводятся все книги, название которых содержит этот фрагмент (регистр не учитывается);
Отображается: название, автор, цена, остаток (только если stock > 0);
Если ничего не найдено — вывести сообщение No matching books found.
Пример ввода:
Enter book title: new
Пример вывода:
Search results:
1. Brave New World by Aldous Huxley — $9.50 (3 in stock)
"""

from task_06 import log_search_query


def search_books_by_title(connection, user_id, db_name, searches_collection):
    fragment = input("Enter book title: ").strip()

    log_search_query(searches_collection, fragment)

    with connection.cursor() as cursor:
        cursor.execute("SELECT title, author, price, stock FROM books WHERE title LIKE %s AND stock > 0 ORDER BY title", (f"%{fragment}%",))
        books = cursor.fetchall()

    if not books:
        print("No matching books found.")
        return

    print("Search results:")
    for i, (title, author, price, stock) in enumerate(books, start=1):
        print(f"{i}. {title} by {author} — ${price:.2f} ({stock} in stock)")


"""Добавьте как пункт 2 в user_menu:"""



