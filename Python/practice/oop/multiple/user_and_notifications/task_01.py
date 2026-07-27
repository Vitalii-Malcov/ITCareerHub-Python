"""
Пользователи и уведомления

01. Система уведомлений
Создайте три класса-миксина, каждый из которых добавляет поддержку одного канала связи:

EmailNotifyMixin
- требует наличие атрибута email
- и реализует метод email_notify(message)

SmsNotifyMixin
- требует наличие атрибута phone
- и реализует метод sms_notify(message)

PushNotifyMixin
- реализует метод push_notify(message)
- и не требует дополнительных атрибутов

Если обязательного атрибута нет, выбрасывайте AttributeError.
"""

class EmailNotifyMixin:
    def email_notify(self, message):
        pass


class SmsNotifyMixin:
    def sms_notify(self, message):
        pass



class PushNotifyMixin:
    pass

