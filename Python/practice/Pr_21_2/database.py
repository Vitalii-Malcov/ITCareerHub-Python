"""
Database — тонкая обёртка над mysql.connector.

Идея: вся "грязная" работа с соединением (открыть, создать БД/таблицы,
закрыть) спрятана в одном классе. Остальной код (репозитории, меню)
просто просит у Database курсор и не знает, откуда он взялся.

Реализует протокол context manager (__enter__/__exit__), поэтому
использовать можно так же естественно, как обычный connection:
    with Database(db_name) as db:
        ...
"""
import mysql.connector
from local_settings_pr_21_2 import dbconfig_write
from queries import books_query, users_query


class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self._connection = None

    def __enter__(self) -> "Database":
        self._connection = mysql.connector.connect(**dbconfig_write)
        self._setup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._connection is not None:
            self._connection.close()
        # False/None — не подавляем исключение, пусть падает наружу как обычно

    @property
    def connection(self):
        if self._connection is None:
            raise RuntimeError("Database is not connected. Use 'with Database(...) as db:'")
        return self._connection

    def cursor(self, buffered: bool = False):
        # buffered=True — чтобы избежать "Unread result found" при
        # последовательных SELECT'ах в репозиториях (частая проблема
        # именно в mysql-connector-python)
        return self.connection.cursor(buffered=buffered)

    def commit(self):
        self.connection.commit()

    def _setup(self):
        with self.cursor() as cursor:
            # CREATE DATABASE IF NOT EXISTS — идемпотентно, безопасно перезапускать
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            cursor.execute("SHOW DATABASES")
            databases = [row[0] for row in cursor]

            if self.db_name in databases:
                print(f"Database '{self.db_name}' created or already exists.")
            else:
                print("Something went wrong. Database not found.")

            cursor.execute(f"USE {self.db_name}")
            cursor.execute(books_query)
            cursor.execute(users_query)

    def list_tables(self) -> list[str]:
        with self.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            return [row[0] for row in cursor]
