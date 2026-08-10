""" 03. Меню книжного магазина

Сделайте этот файл (main.py), главный файлом проекта.
В нём будет размещено основное меню программы.
Каждый раз при запуске этот файл будет
    1. Выполнять код, созданный в предыдущем пункте
    2. В бесконечном цикле запускать пользовательское меню,
     где пользователю будет преложено выбрать 4 цифры:
        1 - загрузить книги из файла (см. пункт 3.1 ниже),
        2 - зарегистрироваться как клиент (см. 3.2),
        3 - войти в свой аккаунт (см. 3.3),
        0 - завершить работу.

Функционал пунктов 1-3 будет выполнен в виде функций.
После выполнения каждого пункта вам необходимо добавить импорт в этот файл (main.py).
"""

import mysql.connector
from local_settings_pr_21 import dbconfig_write
from queries import *
from task_03_1 import load_books_from_file
from task_03_2 import register_user
from task_03_3 import try_login, user_menu

db_name = "010825_bookstore_Vitalii_Malcov"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        with connection.cursor() as cursor:
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

        # Бесконечный цикл главного меню
        while True:
            # Текст главного и пользовательского меню есть в queries.py
            choice = input(text_main_menu).strip()

            if choice == "1":
                filename = input("Enter file name: ")
                load_books_from_file(filename, connection, db_name)

            elif choice == "2":
                register_user(connection, db_name)

            elif choice == "3":
                user_id = try_login(connection, db_name)
                if user_id is not None:
                    user_menu(connection, user_id)

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")



# Database '010825_bookstore_Vitalii_Malcov' created or already exists.
# Tables in '010825_bookstore_Vitalii_Malcov':
# - books
# - users
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 0
# Exiting...
