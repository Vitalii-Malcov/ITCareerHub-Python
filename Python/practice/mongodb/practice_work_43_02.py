""" 02 Сохранение результатов в другую коллекцию

Сохраните все найденные заказы в новую коллекцию orders_lesson_43.
После записи выведите, сколько документов было добавлено.

Пример вывода:
2 documents inserted into 'orders_lesson_43'.

"""

from pymongo import MongoClient
from local_settings_mon import MONGODB_URL_WRITE

with MongoClient(MONGODB_URL_WRITE) as client:
    pass



# {'id': 3, 'customer': 'Olga', 'product': 'Kiwi', 'amount': 9.6, 'city': 'Berlin'}
# {'id': 5, 'customer': 'Olga', 'product': 'Banana', 'amount': 8, 'city': 'Madrid'}
# 2 documents inserted into 'orders_lesson_43'.
# Inserted documents:
# {'_id': ObjectId('695ea6213745118cdc7f6e3f'), 'id': 3, 'customer': 'Olga', 'product': 'Kiwi', 'amount': 9.6, 'city': 'Berlin'}
# {'_id': ObjectId('695ea6213745118cdc7f6e40'), 'id': 5, 'customer': 'Olga', 'product': 'Banana', 'amount': 8, 'city': 'Madrid'}
