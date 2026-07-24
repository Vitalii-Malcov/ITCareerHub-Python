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
from task_01 import Receipt

class Shift:
    pass





    def add_return(self, source_shift: Shift, original_id, return_amount):
        pass


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