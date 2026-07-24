"""Система управления кассовыми чеками

05. Классы SaleReceipt и ReturnReceipt

Доработайте систему чеков:
- создайте 2 дочерних класса
    - SaleReceipt(Receipt) и
    - ReturnReceipt(Receipt)


При создании SaleReceipt
- проверяйте, что сумма положительная

При создании ReturnReceipt
- проверяйте, что сумма отрицательная

В обоих случаях, если сумма нарушает правило, выбрасывается ValueError:
- ValueError("SaleReceipt amount must be positive.")
- ValueError("ReturnReceipt amount must be negative.")

Добавьте метод __str__(), возвращающий строку в формате:
<ReceiptClass> <ID>: +<amount>
<ReceiptClass> <ID>: -<amount>
"""

class Receipt:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
        self._validate()

    def _validate(self):
        pass

    def __str__(self):
        sign = "+" if self.amount > 0 else "-"
        return f"{type(self).__name__}({self.id}:{sign}{abs(self.amount)})"

    def __repr__(self):
        return str(self)


class SaleReceipt(Receipt):
    def _validate(self):
        if self.amount <= 0:
            raise ValueError("SaleReceipt amount must be positive.")


class ReturnReceipt(Receipt):
    def _validate(self):
        if self.amount >= 0:
            raise ValueError("ReturnReceipt amount must be negative.")


if __name__ == "__main__":
    receipts = []

    receipts.append(SaleReceipt(1, 1500))
    receipts.append(SaleReceipt(2, 700))
    receipts.append(ReturnReceipt(3, -300))

    print(receipts)

    print("Общий итог:", sum(r.amount for r in receipts))

# [SaleReceipt 1: +1500, SaleReceipt 2: +700, ReturnReceipt 3: -300]
# Общий итог: 1900
