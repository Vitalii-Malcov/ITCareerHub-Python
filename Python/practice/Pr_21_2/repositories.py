"""
Repository pattern.

Идея: между "бизнес-кодом" (меню, загрузчик книг) и сырым SQL стоит
репозиторий. Он превращает строки из БД в объекты (Book, User) и
наоборот. Если завтра решишь перейти с MySQL на PostgreSQL или добавить
кэш — меняется только реализация репозитория, а не весь проект.

BaseRepository — ABC, задаёт общий контракт (find/save) через
@abstractmethod. Это ровно то, о чём лекция 80: наследование +
репозитории для работы с БД.
"""
from abc import ABC, abstractmethod

from database import Database
from exceptions import InvalidCredentialsError, UsernameAlreadyExistsError
from models import Book, User


class BaseRepository(ABC):
    def __init__(self, db: Database):
        self.db = db

    @abstractmethod
    def find(self, **criteria):
        """Найти одну запись по критериям. Возвращает объект или None."""

    @abstractmethod
    def save(self, entity):
        """Сохранить объект (создать новый или обновить существующий)."""


class BookRepository(BaseRepository):
    def find(self, *, title: str, author: str) -> Book | None:
        with self.db.cursor(buffered=True) as cursor:
            cursor.execute(
                "SELECT id, title, author, price, stock FROM books "
                "WHERE title = %s AND author = %s",
                (title, author),
            )
            row = cursor.fetchone()

        if row is None:
            return None
        return Book(id=row[0], title=row[1], author=row[2], price=row[3], stock=row[4])

    def save(self, book: Book) -> Book:
        # "upsert по смыслу": если книга с таким title+author уже есть —
        # прибавляем stock к существующей записи, иначе создаём новую
        existing = self.find(title=book.title, author=book.author)

        with self.db.cursor() as cursor:
            if existing is not None:
                new_stock = existing.stock + book.stock
                cursor.execute(
                    "UPDATE books SET stock = %s WHERE id = %s",
                    (new_stock, existing.id),
                )
                self.db.commit()
                existing.stock = new_stock
                return existing

            cursor.execute(
                "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)",
                (book.title, book.author, book.price, book.stock),
            )
            self.db.commit()
            book.id = cursor.lastrowid
            return book

    def list_all(self) -> list[Book]:
        with self.db.cursor() as cursor:
            cursor.execute("SELECT id, title, author, price, stock FROM books")
            rows = cursor.fetchall()
        return [Book(id=r[0], title=r[1], author=r[2], price=r[3], stock=r[4]) for r in rows]


class UserRepository(BaseRepository):
    def find(self, *, username: str) -> User | None:
        with self.db.cursor(buffered=True) as cursor:
            cursor.execute(
                "SELECT id, username, password, balance FROM users WHERE username = %s",
                (username,),
            )
            row = cursor.fetchone()

        if row is None:
            return None
        return User(id=row[0], username=row[1], password=row[2], balance=row[3])

    def save(self, user: User) -> User:
        if self.find(username=user.username) is not None:
            raise UsernameAlreadyExistsError(f"Username already exists.")

        with self.db.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password, balance) VALUES (%s, %s, %s)",
                (user.username, user.password, user.balance),
            )
            self.db.commit()
            user.id = cursor.lastrowid
        return user

    def authenticate(self, username: str, password: str) -> User:
        user = self.find(username=username)
        if user is None or user.password != password:
            raise InvalidCredentialsError("Invalid username or password.")
        return user
