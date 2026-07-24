"""Система управления кассовыми чеками

06. Обновление Shift для работы с подклассами чеков

Измените следующие методы в класс Shift:

- Метод add_receipt(amount):
    - должен создавать объекты класса SaleReceipt (вместо Receipt)

- Метод add_return(original_id, return_amount)
    - должен создавать объекты класса ReturnReceipt  (вместо Receipt)

Доработайте уже существующие методы:
- list_receipts(receipt_type=None), который возвращает список всех чеков:
    - Если receipt_type=None — список всех чеков
    - Если receipt_type="sale" — только чеки продаж (SaleReceipt)
    - Если receipt_type="return" — только возвраты (ReturnReceipt)

- get_total(receipt_type=None) который возвращает сумму:
    - Всех чеков, если receipt_type=None
    - Только продаж, если receipt_type="sale"
    - Только возвратов, если receipt_type="return"
"""

from itertools import count
from task_05 import Receipt, SaleReceipt, ReturnReceipt


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


    def add_receipt(self, amount):
        if self.is_closed():
            raise ValueError("Cannot add receipts to a closed shift.")
        receipt = SaleReceipt(next(self._receipt_ids), amount)
        self.receipts.append(receipt)
        return receipt

    def add_return(self, source_shift, original_id, return_amount):
        original_receipt = next((r for r in source_shift.receipts if r.id == original_id), None)
        if original_receipt is None:
            raise ValueError("Original receipt not found.")

        if return_amount > original_receipt.amount:
            raise ValueError("Return amount exceeds original.")

        return_receipt = ReturnReceipt(next(self._receipt_ids), -return_amount)
        self.receipts.append(return_receipt)
        return return_receipt

    def get_total(self, receipt_type=None):
        if receipt_type is None:
            return sum(r.amount for r in self.receipts)
        elif receipt_type == "sale":
            return sum(r.amount for r in self.receipts if isinstance(r, SaleReceipt))
        elif receipt_type == "return":
            return sum(r.amount for r in self.receipts if isinstance(r, ReturnReceipt))
        else:
            raise ValueError("Invalid receipt type. Use 'sale', 'return', or None.")

    def list_receipts(self, receipt_type=None):
        if receipt_type is None:
            print(self.receipts)
        elif receipt_type == "sale":
            print([r for r in self.receipts if isinstance(r, SaleReceipt)])
        elif receipt_type == "return":
            print([r for r in self.receipts if isinstance(r, ReturnReceipt)])
        else:
            raise ValueError("Invalid receipt type. Use 'sale', 'return', or None.")
