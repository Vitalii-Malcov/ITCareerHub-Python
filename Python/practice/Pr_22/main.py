

import mysql.connector
from pymongo import MongoClient

from local_settings_pr_21 import dbconfig_write, MONGODB_URL_WRITE
from queries import *
from functions import load_books_from_file, register_user, try_login, user_menu

db_name = "010825_bookstore_Vitalii_Malcov"


mongo_client = MongoClient(MONGODB_URL_WRITE)
searches_collection = mongo_client["ich_edit"]["010825_bookstore_logs_searches_Vitalii_Malcov"]

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]

        if db_name in databases:
            print(f"Database '{db_name}' created or already exists.")
        else:
            print("Something went wrong. Database not found.")

        cursor.execute(f"USE {db_name}")

        # Шаг 2 — создать таблицы (books, users, purchases — 5. Фиксация покупок)
        cursor.execute(books_query)
        cursor.execute(users_query)
        cursor.execute(purchases_query)

        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor]

        print(f"Tables in '{db_name}':")
        for table in tables:
            print(f"- {table}")

    # Бесконечный цикл главного меню
    while True:
        choice = input(text_main_menu).strip()

        if choice == "1":
            filename = input("Enter file name: ")
            load_books_from_file(filename, connection, db_name)

        elif choice == "2":
            register_user(connection, db_name)

        elif choice == "3":
            user_id = try_login(connection, db_name)
            if user_id is not None:
                user_menu(connection, user_id, db_name, searches_collection)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


# Database '010825_bookstore_Vitalii_Malcov' created or already exists.
# Tables in '010825_bookstore_Vitalii_Malcov':
# - books
# - purchases
# - users
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 0
# Exiting...
