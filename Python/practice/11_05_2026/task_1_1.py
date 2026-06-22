""" 01 Номер покупки

Дан список покупок.
Найдите какой по счету (начиная с единицы) товар с названием "Milk".
Если товара нет, выведите сообщение об отсутствии.

Данные:
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]

Пример вывода:
Товар "Milk" в списке покупок: 4
"""

products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
item = "Milk"

if item in products:
    print(f'Товар "{item}" в списке покупок: {products.index(item) + 1}')
else:
    print(f'Товар "{item}" отсутствует в списке покупок')

