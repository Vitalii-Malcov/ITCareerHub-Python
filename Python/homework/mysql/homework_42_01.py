""" 01 Создание базы

Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""

import mysql.connector
from local_settings_hw import dbconfig_write


class DatabaseConnection:
    """
    Этот класс умеет только одно: открывать и закрывать соединение с MySQL.

    ИНКАПСУЛЯЦИЯ здесь в том, что снаружи никто напрямую не трогает
    mysql.connector - вся "грязная работа" с библиотекой спрятана внутри
    класса, а наружу класс отдаёт только удобные методы.
    """

    def __init__(self, config):
        self._config = config

        self._connection = None

    def __enter__(self):
        self._connection = mysql.connector.connect(**self._config)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection is not None:
            self._connection.close()

    def cursor(self, dictionary=False):
        return self._connection.cursor(dictionary=dictionary)

    def commit(self):
        # commit() сохраняет изменения (INSERT/UPDATE/DELETE) в базе окончательно
        self._connection.commit()


class DatabaseInitializer:
    """
    Этот класс отвечает только за создание базы данных.

    КОМПОЗИЦИЯ здесь в том, что DatabaseInitializer НЕ ЯВЛЯЕТСЯ соединением,
    а просто ХРАНИТ ссылку на уже готовый объект DatabaseConnection
    (получает его как параметр в __init__) и пользуется им.
    """

    def __init__(self, connection, db_name):
        self._connection = connection

        self._db_name = db_name

    def create(self):
        cursor = self._connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self._db_name}")

        cursor.execute(f"USE {self._db_name}")

        cursor.close()

        print(f"Database '{self._db_name}' created or already exists.")


if __name__ == "__main__":
    db_name = "060326_ptm_vitalii_malcov_hw"

    with DatabaseConnection(dbconfig_write) as db:
        initializer = DatabaseInitializer(db, db_name)

        initializer.create()

# Database '060326-ptm_vitalii_malcov_hw' created or already exists.
