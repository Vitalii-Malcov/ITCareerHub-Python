""" Система управления кассовыми чеками

01. Класс Receipt
Создайте класс Receipt, представляющий чек.
Каждый чек должен иметь ID и сумму.
Метод __str__() должен возвращать строку формата:
Receipt <ID>: <amount>
"""
class Receipt:
    __slots__ = ('id', 'amount')
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    def __str__(self):
        return "Receipt {}: {}".format(self.id, self.amount)

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    receipt = Receipt(1, 100)
    print(receipt)

    # Receipt 1: 100
