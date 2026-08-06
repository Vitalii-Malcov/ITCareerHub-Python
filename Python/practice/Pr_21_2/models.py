"""
Модели предметной области.

Почему dataclass, а не просто кортеж/словарь из БД:
- автогенерируются __init__, __repr__, __eq__;
- __post_init__ даёт место, куда положить валидацию/нормализацию
  (например, деньги — сразу переводим в Decimal, чтобы не словить
  ошибки округления float при работе с ценой/балансом);
- методы вроде in_stock / can_afford живут рядом с данными,
  а не размазаны по коду меню.
"""
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Book:
    title: str
    author: str
    price: Decimal
    stock: int
    id: int | None = None  # None, пока книга не сохранена в БД (id ещё не назначен)

    def __post_init__(self):
        # Decimal(str(...)) — правильный способ; Decimal(0.1) напрямую
        # унаследует погрешность float, а Decimal(str(0.1)) — нет
        self.price = Decimal(str(self.price))

    @property
    def in_stock(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        return f"{self.title} by {self.author} — {self.price}€ ({self.stock} in stock)"


@dataclass
class User:
    username: str
    password: str
    balance: Decimal
    id: int | None = None

    def __post_init__(self):
        self.balance = Decimal(str(self.balance))

    def can_afford(self, amount: Decimal) -> bool:
        return self.balance >= amount

    def __str__(self) -> str:
        return f"User #{self.id} ({self.username}), balance={self.balance}€"
