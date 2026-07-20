""" 01 Счётчик экземпляров

Создайте класс User, представляющий пользователя.
При создании должны указываться
- логин (username)
- и пароль (password).

У класса должно быть поле
- total_users, хранящее общее количество созданных пользователей.

При каждом создании нового объекта User, счётчик должен увеличиваться.

Добавьте метод
- get_total(), возвращающий количество пользователей.
Проверьте, что счётчик работает.

Пример вывода:
Total users: 2
"""
from itertools import count


class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users


class User_2:
    total_users = 0

    def __new__(cls, *args, **kwargs):
        cls.total_users += 1
        return super().__new__(cls)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_total(cls):
        return cls.total_users


class User_3:
    _counter = count(1)
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = next(User_3._counter)
        User_3.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

class User_4:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User_4.total_users += 1
        
    @property
    def total(self):
        return User_4.total_users

user1 = User("alice", "pass123")
user2 = User("bob", "secure456")

print(f"Total users: {User.get_total()}")
print(f"Total users: {user1.get_total()}")
print(f"Total users: {user2.get_total()}")

# Total users: 2
