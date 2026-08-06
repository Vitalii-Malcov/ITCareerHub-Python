""" 01. Поиск заказов с маленькой суммой

Прочитайте все документы из коллекции ich_edit.orders, у которых сумма (amount) меньше 10.
Выведите каждый найденный заказ построчно.

Пример вывода:
{'_id': ObjectId('...'), 'id': 3, 'customer': 'Olga', 'product': 'Kiwi', 'amount': 9.6, 'city': 'Berlin'}
{'_id': ObjectId('...'), 'id': 5, 'customer': 'Olga', 'product': 'Banana', 'amount': 8, 'city': 'Madrid'}
"""

from pymongo import MongoClient
from local_settings_mon import MONGODB_URL_WRITE

with MongoClient(MONGODB_URL_WRITE) as client:
    pass


# {'id': 3, 'customer': 'Olga', 'product': 'Kiwi', 'amount': 9.6, 'city': 'Berlin'}
# {'id': 5, 'customer': 'Olga', 'product': 'Banana', 'amount': 8, 'city': 'Madrid'}
