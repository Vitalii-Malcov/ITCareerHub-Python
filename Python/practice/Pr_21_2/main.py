"""
Точка входа. Специально короткая — вся логика уже разложена по классам,
здесь только "собрать всё вместе и запустить".
"""
from database import Database
from menu import MainMenu

DB_NAME = "060326_bookstore_Vitalii"


def main():
    with Database(DB_NAME) as db:
        print(f"Tables in '{DB_NAME}':")
        for table in db.list_tables():
            print(f"- {table}")

        MainMenu(db).run()


if __name__ == "__main__":
    main()
