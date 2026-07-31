""" 01 Электронное письмо — несколько вариантов реализации

Реализуйте класс Email, который представляет электронное письмо.
Каждое письмо должно содержать:
- sender — адрес отправителя
- recipient — адрес получателя
- subject — тема письма
- body — текст письма
- date — дата отправки

Класс должен поддерживать:
- Сравнение писем по дате
- Преобразование письма в строку
- Получение длины текста письма
- Проверку на наличие текста в письме или не состоит ли текст только из пробелов

Пример вывода (одинаков для всех вариантов):
From: alice@example.com
To: bob@example.com
Subject: Meeting
- Let's meet at 10am -

From: bob@example.com
To: alice@example.com
Subject: Report
-  -

Length: 18
Has text: True
Is newer: True
"""

from datetime import datetime
from functools import total_ordering
from dataclasses import dataclass


class Email1:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        # Формируем многострочное представление письма
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        # Длина текста письма (длина body)
        return len(self.body)

    def __bool__(self):
        # True, если текст не пустой и не состоит только из пробелов
        return bool(self.body.strip())

    def __gt__(self, other):
        # Сравнение писем по дате
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

    def __eq__(self, other):
        return self.date == other.date


# ---------------------------------------------------------------------------
@total_ordering  # достраивает __le__, __gt__, __ge__ на основе __eq__ и __lt__
class Email2:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        # total_ordering сам выведет __gt__, __le__, __ge__ из этого метода
        return self.date < other.date


# ---------------------------------------------------------------------------
class Email3:
    def __init__(self, sender, recipient, subject, body, date):
        self._sender = sender
        self._recipient = recipient
        self._subject = subject
        self._body = body
        self._date = date

    @property
    def body(self):
        return self._body

    @property
    def date(self):
        return self._date

    def __str__(self):
        return (
            f"From: {self._sender}\n"
            f"To: {self._recipient}\n"
            f"Subject: {self._subject}\n"
            f"- {self._body} -"
        )

    def __len__(self):
        return len(self._body)

    def __bool__(self):
        # strip() убирает пробелы, чтобы "   " считалось пустым текстом
        return bool(self._body.strip())

    def __gt__(self, other):
        if not isinstance(other, Email3):
            return NotImplemented
        return self._date > other._date


# ---------------------------------------------------------------------------
@dataclass
class Email4:
    sender: str
    recipient: str
    subject: str
    body: str
    date: datetime

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

    # dataclass сам генерирует __eq__ по ВСЕМ полям (не только по date),
    # если это не нужно — можно переопределить __eq__ вручную


# ---------------------------------------------------------------------------
class Email5:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __repr__(self):
        # техническое представление — удобно для отладки в консоли
        return f"Email5(sender={self.sender!r}, subject={self.subject!r}, date={self.date!r})"

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __contains__(self, word):
        # позволяет писать: "meet" in e1
        return word in self.body

    def __eq__(self, other):
        return self.date == other.date

    def __lt__(self, other):
        return self.date < other.date

    def __hash__(self):
        # нужно явно определить, т.к. при наличии __eq__ хэш по умолчанию убирается
        return hash((self.sender, self.recipient, self.date))


# ---------------------------------------------------------------------------
class Email6:
    def __init__(self, sender, recipient, subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self):
        return (
            f"From: {self.sender}\n"
            f"To: {self.recipient}\n"
            f"Subject: {self.subject}\n"
            f"- {self.body} -"
        )

    def __len__(self):
        return len(self.body)

    def __bool__(self):
        return bool(self.body.strip())

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

    def __eq__(self, other):
        return self.date == other.date

    def __add__(self, other):
        # e1 + e2 -> объединённый текст переписки (пример нестандартного применения)
        return f"{self}\n\n{other}"

    def __format__(self, spec):
        # поддержка форматирования: f"{e1:short}"
        if spec == "short":
            return f"{self.subject} ({self.date.date()})"
        return str(self)



if __name__ == "__main__":
    classes = [Email1, Email2, Email3, Email4, Email5, Email6]

    for i, EmailClass in enumerate(classes, start=1):
        print(f"===== Вариант {i}: {EmailClass.__name__} =====")

        e1 = EmailClass("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
        e2 = EmailClass("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

        print(e1)
        print()
        print(e2)
        print()
        print("Length:", len(e1))
        print("Has text:", bool(e1))
        print("Is newer:", e2 > e1)
        print()
