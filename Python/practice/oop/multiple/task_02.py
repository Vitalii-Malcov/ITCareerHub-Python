"""Система управления кассовыми чеками

02. Класс Shift

Создайте класс Shift, представляющий кассовую смену.
У каждой смены
- свой уникальный ID: _id_counter (нумерация с 1)

Кроме того, у смены есть:
- список чеков
- статус (открыта или закрыта)

Реализуйте методы:
- is_closed() — возвращает закрыта ли смена
- close() — закрывает смену
- get_total() — возвращает сумму всех чеков
- list_receipts() — выводит список чеков через print()
"""

class Shift:
    _id_counter = 0

    @classmethod
    def _next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

    def __init__(self):
        self.id = Shift._next_id()
        self.receipts = []
        self.status = "Open"

    def is_closed(self):
        return self.status == "Closed"

    def close(self):
        self.status = "Closed"

    def get_total(self):
        return sum(r.amount for r in self.receipts)

    def list_receipts(self):
        print(self.receipts)


