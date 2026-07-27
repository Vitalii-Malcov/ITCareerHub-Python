"""Система управления кассовыми чеками

07. Проверка всей системы

Проверьте работу всей логики:
- Создайте смену и добавьте 2 чека на продажу
- Создайте вторую смену и выполните возврат по одному из чеков первой
- Отобразите списки и суммы всех чеков по типам
- Убедитесь, что возврат нельзя выполнить с неверной суммой
Пример вывода:
SaleReceipt 1: +100
SaleReceipt 2: +200
ReturnReceipt 1: -50
Total sales: 300
Total returns: -50
Total: 250
"""

from task_06 import Shift

# Создание первой смены
shift1 = Shift()
shift1.add_receipt(100)
shift1.add_receipt(200)

# Создание второй смены
shift2 = Shift()
shift2.add_return(shift1, 1, 50)

# Вывод чеков обеих смен
shift1.list_receipts()
shift2.list_receipts()

# Подсчёт сумм по второй смене
print("Total sales shift2:", shift2.get_total(receipt_type="sale"))
print("Total returns shift2:", shift2.get_total(receipt_type="return"))
print("Total shift2:", shift2.get_total())

# Попытка сделать неверный возврат (слишком большая сумма)
try:
    shift2.add_return(shift1, 1, 500)
except ValueError as e:
    print("Error:", e)


# [SaleReceipt 1: +100, SaleReceipt 2: +200]
# [ReturnReceipt 1: -50]
# Total sales shift2: 0
# Total returns shift2: -50
# Total shift2: -50
# Error: Return amount exceeds original.