"""
Практические задания 21
Лекция 42 - MySQL. Транзакции
Онлайн-магазин книг
Вы создаёте пошагово консольное приложение на Python, работающее с базой данных MySQL и MongoDB. Программа имитирует работу интернет-магазина книг — с регистрацией пользователей, загрузкой и покупкой книг, а также отслеживанием поисковых запросов.
Проект включает в себя следующие этапы:
 - Создание базы данных и таблиц
 - Реализация меню магазина с загрузкой данных из файла и регистрацией клиентов
 - Реализация входа в аккаунт и дополнительного меню клиента
 - Просмотр и покупка книг
 - Фиксация покупок в таблице
 - Фиксация поисков в MongoDB
 - Анализ самых популярных запросов
 - Разделение программы на модули

Онлайн-магазин книг. Часть 1

1. Создание книжного магазина

Создайте новую базу данных под названием 010825_bookstore_<your_name>
После этого выполните проверку:
- если база данных успешно создана (или уже существует), выведите сообщение:
  Database 'bookstore' created or already exists.
"""
import mysql.connector
from local_settings_pr_21 import dbconfig_write

def show_or_create_db(cur, database_name):
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")  # Создать БД db_name
    cur.execute("SHOW DATABASES")
    databases = [row[0] for row in cur]  # Получение списка БД

    if database_name in databases:  # проверить, если ваша БД в списке всех БД databases
        print(f"Database '{database_name}' created or already exists.")
    else:
        print("Something went wrong. Database not found.")


db_name = "060326_bookstore_Vitalii_Malcov"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        show_or_create_db(cursor, db_name)


# Database '060326_bookstore_Vitalii_Malcov' created or already exists.
