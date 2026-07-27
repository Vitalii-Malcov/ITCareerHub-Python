""" Пользователи и уведомления

02. Получатели уведомлений

Создайте базовый класс User, представляющий пользователя с name.

На его основе реализуйте два типа пользователей:
Courier
- дополнительно принимает
    - email
    - и phone,
- и в методе notify() поддерживает:
    - email-уведомления
    - SMS-уведомления

Admin
- в методе notify() поддерживает только push-уведомления

Таким образом, каждый класс (и Courier, и Admin) должен иметь метод notify(message),
который вызывает соответствующие заданию типы уведомлений.

При реализации наследуйте классы, соответствующие типам уведомлений.
Пример вывода:
Email to alice@example.com: Package delivered.
SMS to +123456789: Package delivered.
Push notification: New report available.
"""
from task_01 import EmailNotifyMixin, SmsNotifyMixin, PushNotifyMixin

class User:
    pass


class Courier(   ):
    pass


class Admin(   ):
    pass



courier = Courier("Alice", "alice@example.com", "+123456789")
admin = Admin("Bob")

courier.notify("Package delivered.")
admin.notify("New report available.")

# Email to alice@example.com: Package delivered.
# SMS to +123456789: Package delivered.
# Push notification: New report available.