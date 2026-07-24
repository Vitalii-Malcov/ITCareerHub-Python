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
from task_01 import Receipt

class Shift:
    pass



    def add_receipt(self, amount):
        pass



if __name__ == "__main__":
    shift = Shift()
    shift.add_receipt(100)
    shift.add_receipt(200)
    shift.add_receipt(100)
    shift.list_receipts()
    print(shift.get_total())


# [Receipt 1: 100, Receipt 2: 200, Receipt 3: 100]
# 400