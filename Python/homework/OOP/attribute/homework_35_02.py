""" 02. Проверка данных пользователя

Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.
"""


class UserV1:
    total_users = 0

    def __init__(self, username, password):
        self._validate(username, password)  # выносим проверки в отдельный метод
        self.username = username
        self.password = password
        UserV1.total_users += 1

    @staticmethod
    def _validate(username, password):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой.")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError("Пароль должен быть строкой длиной не менее 5 символов.")

    def __str__(self):
        return f"User(username='{self.username}')"

    @classmethod
    def get_total(cls):
        return cls.total_users

# ======================================================================

class UserV2:
    total_users = 0

    def __init__(self, username, password):
        self.username = username  # вызовет setter -> validate
        self.password = password  # вызовет setter -> validate
        UserV2.total_users += 1

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя пользователя должно быть непустой строкой.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 5:
            raise ValueError("Пароль должен быть строкой длиной не менее 5 символов.")
        self._password = value

    def __str__(self):
        return f"User(username='{self.username}')"

    @classmethod
    def get_total(cls):
        return cls.total_users


# ======================================================================

class InvalidUsernameError(ValueError):
    """Некорректное имя пользователя."""
    pass


class InvalidPasswordError(ValueError):
    """Некорректный пароль."""
    pass


class UserV3:
    total_users = 0
    MIN_PASSWORD_LEN = 5  # вынесли константу — легко поменять правило

    def __init__(self, username, password):
        if not isinstance(username, str) or not username.strip():
            raise InvalidUsernameError("Имя пользователя должно быть непустой строкой.")
        if not isinstance(password, str) or len(password) < self.MIN_PASSWORD_LEN:
            raise InvalidPasswordError(
                f"Пароль должен быть строкой длиной не менее {self.MIN_PASSWORD_LEN} символов."
            )

        self.username = username
        self.password = password
        UserV3.total_users += 1

    def __str__(self):
        return f"User(username='{self.username}')"

    def __repr__(self):  # заодно repr — пригодится для списков/отладки
        return f"User(username={self.username!r}, total={UserV3.total_users})"

    @classmethod
    def get_total(cls):
        return cls.total_users



# ТЕСТЫ — прогоняем одинаковый сценарий для всех трёх вариантов


def run_tests(user_class, label):
    print(f"\n--- {label} ---")

    try:
        user1 = user_class("alice", "pass123")
        print(user1)  # User(username='alice')
    except ValueError as e:
        print("Error:", e)

    try:
        user2 = user_class("", "12345")  # Некорректное имя
    except ValueError as e:
        print("Error:", e)

    try:
        user3 = user_class("bob", "123")  # Слишком короткий пароль
    except ValueError as e:
        print("Error:", e)

    print(f"Total users: {user_class.get_total()}")
    # Должно быть 1, только валидные пользователи считаются


if __name__ == "__main__":
    run_tests(UserV1, "Вариант 1: базовый")
    run_tests(UserV2, "Вариант 2: через property")
    run_tests(UserV3, "Вариант 3: кастомные исключения")

    print("\n--- Вариант 3: отлов конкретных исключений ---")
    try:
        UserV3("", "12345")
    except InvalidUsernameError as e:
        print("Поймали именно InvalidUsernameError:", e)

    try:
        UserV3("bob", "123")
    except InvalidPasswordError as e:
        print("Поймали именно InvalidPasswordError:", e)


# User(username='alice')
# Error: Username must be a non-empty string.
# Error: Password must be a string with at least 5 characters.
# Total users: 1
