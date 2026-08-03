""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

"""

from local_settings_hw import dbconfig_write
from homework_42_01 import DatabaseConnection, DatabaseInitializer


class BaseRepository:
    """
    Базовый класс для всех "репозиториев" (классов, которые работают
    с какой-то одной таблицей в базе данных).

    Здесь только одна общая вещь: любой репозиторий хранит ссылку
    на соединение с базой (снова КОМПОЗИЦИЯ - репозиторий "имеет"
    соединение, а не "является" им).
    """

    def __init__(self, connection):
        # Сохраняю соединение - им будут пользоваться дочерние классы
        self.connection = connection


class NotesRepository(BaseRepository):
    """
    Репозиторий для работы с таблицей notes.

    НАСЛЕДОВАНИЕ здесь в том, что этот класс написан как
    "class NotesRepository(BaseRepository)" - значит, он автоматически
    получает всё, что есть в BaseRepository (метод __init__ с self.connection),
    и не должен писать это заново.
    """

    def create_table(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT
            )
        """)

        cursor.close()

    def insert(self, title, content):
        cursor = self.connection.cursor()

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s)",
            (title, content)
        )

        cursor.close()

    def get_all(self):
        cursor = self.connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM notes")

        rows = cursor.fetchall()

        cursor.close()

        return rows


if __name__ == "__main__":
    db_name = "060326_ptm_vitalii_malcov_hw"

    # Открываю одно соединение и использую его для всего:
    # и для создания базы, и для работы с таблицей notes
    with DatabaseConnection(dbconfig_write) as db:
        # Шаг 1: создаю базу данных (тот же класс, что и в 01)
        DatabaseInitializer(db, db_name).create()

        # Шаг 2: создаю объект репозитория для таблицы notes
        notes_repo = NotesRepository(db)

        # Шаг 3: создаю таблицу notes
        notes_repo.create_table()

        # Шаг 4: вставляю одну заметку
        notes_repo.insert("First Note", "This is the content of my first note.")

        # Шаг 5: сохраняю изменения в базе (без commit() данные не сохранятся!)
        db.commit()

        # Шаг 6: вывожу все заметки
        print("\nAll notes:")
        for note in notes_repo.get_all():
            print(note)

# Database '060326_ptm_vitalii_malcov_hw' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
