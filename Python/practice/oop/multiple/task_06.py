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

from task_05 import Receipt, SaleReceipt, ReturnReceipt

class Shift:
    pass



    def add_receipt(self, amount):
        pass

    def add_return(self, source_shift, original_id, return_amount):
        pass


