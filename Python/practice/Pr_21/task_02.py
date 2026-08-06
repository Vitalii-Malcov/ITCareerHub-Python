""" 02. Создание таблиц для магазина

Расширьте предыдущую программу:
    после создания базы данных, создайте в ней две таблицы:
        books — для хранения информации о книгах;
        users — для регистрации клиентов.

Код для создания таблиц:
books_query = '''
   CREATE TABLE IF NOT EXISTS books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(200),
       author VARCHAR(100),
       price DECIMAL(10, 2),
       stock INT CHECK (stock >= 0)
   )
'''

users_query = '''
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(100),
       password VARCHAR(100),
       balance DECIMAL(10, 2) CHECK (balance >= 0)
   )
'''
После создания таблиц выведите список всех таблиц в текущей базе.
Пример вывода: 
Tables in 'bookstore':
- books
"""

import mysql.connector
from local_settings_pr_21 import dbconfig_write
from queries import *

db_name = "010825_bookstore_Vitalii_Malcov"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]  # Получение списка БД

        if db_name in databases:  # проверить, если ваша БД в списке всех БД databases
            print(f"Database '{db_name}' created or already exists.")
        else:
            print("Something went wrong. Database not found.")

        cursor.execute(f"USE {db_name}")  # Переключение на созданную базу данных

        # Шаг 2 — создать таблицы
        # Готовые запросы есть в queries.py!

        # Вывод списка таблиц
        cursor.execute(books_query)
        cursor.execute(users_query)

        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor]

        print(f"Tables in '{db_name}':")
        for table in tables:
            print(f"- {table}")


# Database '010825_bookstore_Vitalii_Malcov' created or already exists.
# Tables in '010825_bookstore_Vitalii_Malcov':
# - books
# - users
