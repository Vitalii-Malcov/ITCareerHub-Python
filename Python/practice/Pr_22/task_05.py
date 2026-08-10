""" 5. Фиксация покупок

Добавьте в базу данных таблицу purchases, которая будет фиксировать все совершённые покупки.
Код для создания таблиц:
purchases_query = '''
    CREATE TABLE IF NOT EXISTS purchases (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        book_id INT,
        quantity INT,
        purchase_date DATE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
'''
Таблица должна быть создана в базе bookstore;
При каждой успешной покупке данные должны сохраняться в эту таблицу.

"""
# Решение: в файле main добавляем cоздание таблицы покупок (после книг и пользователя)


# Обновление функции purchase_book: В конец функции добавьте сохранение в таблицу purchases:
# Добавление в журнал покупок

# Это делается после успешного списания книги и баланса.

