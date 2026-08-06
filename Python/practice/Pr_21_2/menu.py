"""
Меню через паттерн Template Method.

Menu.run() — "скелет" алгоритма: показать текст меню, спросить выбор,
выполнить действие, повторить. Этот скелет один и тот же для главного
меню и для меню пользователя — поэтому он написан один раз в базовом
классе и не дублируется.

Подклассы (MainMenu, UserMenu) переопределяют только "переменные части":
какой текст показывать и какие действия стоят за какими цифрами.
Это и есть суть Template Method — общий алгоритм наверху, детали внизу.

Действие возвращает False, если после него нужно выйти из цикла меню
(Exit / Logout); любое другое значение (включая None) — просто продолжаем.
"""
from abc import ABC, abstractmethod
from typing import Callable

from database import Database
from exceptions import InvalidCredentialsError, UsernameAlreadyExistsError
from models import User
from queries import text_main_menu, text_user_menu
from repositories import BookRepository, UserRepository
from services import BookLoader


class Menu(ABC):
    def __init__(self):
        self.actions: dict[str, Callable[[], object]] = self._build_actions()

    @abstractmethod
    def menu_text(self) -> str:
        """Текст, который печатается перед вводом выбора."""

    @abstractmethod
    def _build_actions(self) -> dict[str, Callable[[], object]]:
        """Словарь {'1': self.some_method, ...}."""

    def run(self):
        while True:
            choice = input(self.menu_text())
            action = self.actions.get(choice)

            if action is None:
                print("Invalid choice, try again.")
                continue

            if action() is False:
                break


class MainMenu(Menu):
    def __init__(self, db: Database):
        self.db = db
        self.book_repo = BookRepository(db)
        self.user_repo = UserRepository(db)
        self.book_loader = BookLoader(self.book_repo)
        super().__init__()  # actions строятся уже после того, как репозитории готовы

    def menu_text(self) -> str:
        return text_main_menu

    def _build_actions(self) -> dict[str, Callable[[], object]]:
        return {
            "1": self._load_books,
            "2": self._register,
            "3": self._login,
            "0": self._exit,
        }

    def _load_books(self):
        filename = input("Enter file name: ")
        added = self.book_loader.load_from_file(filename)
        print(f"{added} books loaded.")

    def _register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            balance = float(input("Enter initial balance: "))
        except ValueError:
            print("Invalid balance.")
            return

        try:
            self.user_repo.save(User(username=username, password=password, balance=balance))
        except UsernameAlreadyExistsError:
            print("Username already exists.")
            return

        print("Registration successful.")

    def _login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            user = self.user_repo.authenticate(username, password)
        except InvalidCredentialsError as error:
            print(error)
            return

        print("Login successful.")
        UserMenu(self.db, user).run()  # вложенный цикл меню — вернёт управление сюда после Logout

    def _exit(self):
        print("Exiting...")
        return False


class UserMenu(Menu):
    def __init__(self, db: Database, user: User):
        self.db = db
        self.user = user
        super().__init__()

    def menu_text(self) -> str:
        return text_user_menu.format(user_id=self.user.id)

    def _build_actions(self) -> dict[str, Callable[[], object]]:
        return {
            "1": self._view_books,
            "2": self._search_books,
            "3": self._purchase_book,
            "4": self._view_frequent_queries,
            "0": self._logout,
        }

    # Пункты 1-4 — заглушки, логика появится в следующих частях задания
    def _view_books(self):
        print("Books will be shown here.")

    def _search_books(self):
        print("Search will be shown here.")

    def _purchase_book(self):
        print("Purchase will be shown here.")

    def _view_frequent_queries(self):
        print("Frequent queries will be shown here.")

    def _logout(self):
        return False
