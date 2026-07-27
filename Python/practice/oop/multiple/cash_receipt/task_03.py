"""Система управления кассовыми чеками

03 Добавление чеков

Доработайте Shift, чтобы
- чеки создавались только (!) через смену
    (композиция или агрегация?)

А именно:
- добавьте в Shift метод add_receipt(), который:
    - Создаёт объект Receipt с уникальным ID
        (ID чека уникален только в рамках текущей смены,
         каждая новая смена начинается с чека #1)
    - Сохраняет его внутри текущей смены
    - Если смена закрыта — выбрасывается ValueError:
        - ValueError("Cannot add receipts to a closed shift.")

Проверьте работу метода, создав несколько чеков внутри смены.
"""
from itertools import count
from task_01 import Receipt

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
        self._receipts_ids = count(1)

    def is_closed(self):
        return self.status == "Closed"

    def close(self):
        self.status = "Closed"

    def get_total(self):
        return sum(r.amount for r in self.receipts)

    def list_receipts(self):
        print(self.receipts)

    def add_receipt(self, amount):
        if self.is_closed():
            raise ValueError("Cannot add receipts to a closed shift.")
        receipt = Receipt(next(self._receipts_ids), amount)
        self.receipts.append(receipt)
        return receipt

if __name__ == "__main__":
    shift = Shift()
    shift.add_receipt(100)
    shift.add_receipt(200)
    shift.add_receipt(100)
    shift.list_receipts()
    print(shift.get_total())


# [Receipt 1: 100, Receipt 2: 200, Receipt 3: 100]
# 400
