"""Система управления кассовыми чеками

04. Возврат по чеку

Доработайте Shift:

Добавьте метод add_return(shift, original_id, return_amount), где:
- shift: объект смены, в которой была покупка,
- original_id: ID исходного чека
- return_amount: сумму возврата

Метод проверяет,
- что в переданной смене существует чек с таким ID,
- в противном случае выбрасывается исключение:
    - ValueError("Original receipt not found.")

- что сумма возврата не превышает сумму этого чека
- в противном случае выбрасывается исключение:
    ValueError("Return amount exceeds original.")


Метод создаёт
- новый чек с отрицательной (!!!) суммой и

Метод добавляет
- этот созданные возвратный чек в текущую смену, как и обычные чеки
"""
from __future__ import annotations
from itertools import count

from dns.asyncquery import receive_tcp

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
        self.status = "OPEN"
        self._receipt_ids = count(1)

    def is_closed(self):
        return self.status == "CLOSED"

    def close(self):
        self.status = "CLOSED"

    def get_total(self):
        return sum(r.amount for r in self.receipts)

    def list_receipts(self):
        print(self.receipts)

    def add_receipt(self, amount):
        if self.is_closed():
            raise ValueError("Cannot add receipts to a closed shift.")
        receipt = Receipt(next(self._receipt_ids), amount)
        self.receipts.append(receipt)
        return receipt


    def add_return(self, source_shift: Shift, original_id, return_amount):
        if self.is_closed():
            raise ValueError("Cannot add receipts to a closed shift.")

        original_receipt = next((r for r in source_shift.receipts if r.id == original_id), None)
        if original_receipt is None:
            raise ValueError("Original receipt not found.")

        if return_amount > original_receipt.amount:
            raise ValueError("Return amount exceeds original.")


        return_receipt = Receipt(next(self._receipt_ids), -return_amount)
        self.receipts.append(return_receipt)
        return return_receipt

if __name__ == "__main__":
    shift1 = Shift()

    shift1.add_receipt(1000)
    shift1.add_receipt(2500)
    shift1.add_receipt(700)

    print("Смена #", shift1.id)
    print("Сумма:", shift1.get_total())

    shift1.close()

    shift2 = Shift()
    shift2.add_return(shift1, 2, 500)

    print("\nСмена #", shift2.id)
    shift2.list_receipts()
    print("Сумма:", shift2.get_total())


# Смена # 1
# Сумма: 4200
#
# Смена # 2
# Receipt 1: -500
# Сумма: -500
