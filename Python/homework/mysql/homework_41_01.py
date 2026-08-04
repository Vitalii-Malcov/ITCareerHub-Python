
""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

Попробуйте решить задачи используя стиль Data Access Object (DAO).
"""

import mysql.connector
from local_settings_hw import dbconfig


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""


class MySQLConnection:
    """
    Базовый класс — отвечает ТОЛЬКО за подключение к MySQL.
    Реализует протокол контекстного менеджера (with ... as db),
    поэтому соединение и курсор гарантированно закрываются
    даже если внутри блока произойдёт ошибка.
    """

    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.dbconfig)
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as e:
            raise DatabaseError(f"Не удалось подключиться к базе данных: {e}") from e
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()
        return False


class WorldDB(MySQLConnection):
    """
    DAO для базы world: содержит только методы-запросы,
    сама логика подключения унаследована от MySQLConnection.
    """

    def fetch_countries(self):
        """Получить список всех стран (по алфавиту)"""
        try:
            self.cursor.execute("SELECT Name FROM country ORDER BY Name")
            rows = self.cursor.fetchall()
            return [row["Name"] for row in rows]
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при получении списка стран: {e}")


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
