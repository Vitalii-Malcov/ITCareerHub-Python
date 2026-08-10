""" 4.3. Покупка книги
Добавьте в меню клиента возможность купить книгу из списка доступных.
Пользователь видит список всех книг в наличии;
Затем вводит номер книги и количество;
Если книги недостаточно — вывести сообщение Not enough books in stock.;
Если денег недостаточно — вывести сообщение Insufficient funds.;
Если всё успешно — списывается количество книг и сумма с баланса пользователя;
После успешной покупки — вывести сообщение Purchase successful.
Пример ввода:
Enter book number: 1
Enter quantity: 2
Пример вывода:
Purchase successful.
"""

def purchase_book(connection, user_id, db_name):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, title, author, price, stock FROM books WHERE stock > 0 ORDER BY title"
        )
        books = cursor.fetchall()

    if not books:
        print("No books available.")
        return

    print("Available books:")
    for i, (book_id, title, author, price, stock) in enumerate(books, start=1):
        print(f"{i}. {title} by {author} — ${price:.2f} ({stock} in stock)")

    try:
        number = int(input("Enter book number: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input.")
        return

    book_id, title, author, price, stock = books[number-1]

    if not (1 <= number <= len(books)) or quantity <= 0:
        print("Not enough books in stock.")
        return

    total_price = price * quantity

    with connection.cursor() as cursor:
        cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
        row = cursor.fetchone()
        if row is None:
            print("User not found.")
            return
        (balance, ) = row

        if balance < total_price:
            print("Insufficient funds.")
            return

        # списываем количество книг и сумму с баланса пользователя
        cursor.execute(
            "UPDATE books SET stock = stock - %s WHERE id = %s", (quantity, book_id)
        )
        cursor.execute(
            "UPDATE users SET balance = balance - %s WHERE id = %s", (total_price, user_id)
        )

        cursor.execute(
            "INSERT INTO purchases (user_id, book_id, quantity, purchase_date) VALUES (%s, %s, %s, %s)",
            (user_id, book_id, quantity)
        )

        connection.commit()
    print("Purchase successful.")

"""Добавьте как пункт 3 в user_menu:"""

