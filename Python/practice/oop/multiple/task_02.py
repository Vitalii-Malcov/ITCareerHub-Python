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
    _id_counter = ...

    def __init__(self):
        pass

    def is_closed(self):
        pass

    def close(self):
        pass

    def get_total(self):
        pass

    def list_receipts(self):
        pass


