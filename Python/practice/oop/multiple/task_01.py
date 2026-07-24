""" Система управления кассовыми чеками

01. Класс Receipt
Создайте класс Receipt, представляющий чек.
Каждый чек должен иметь ID и сумму.
Метод __str__() должен возвращать строку формата:
Receipt <ID>: <amount>
"""
class Receipt:
    pass


if __name__ == "__main__":
    receipt = Receipt(1, 100)
    print(receipt)

    # Receipt 1: 100
