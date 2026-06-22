""" 01 Выбор заказов
У вас есть список заказов.
Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
- Отбирает заказы дороже 500.
- Создаёт список названий отобранных продуктов в алфавитном порядке.
- Возвращает итоговый список названий.
Данные:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
Пример вывода:
['Chair', 'Laptop']
"""
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

sample = ['Chair', 'Laptop']


def select_expensive_orders(ords):
    expensive_orders = filter(lambda order: order["price"] > 500, ords)
    product_names = map(lambda order: order["product"], expensive_orders)
    return sorted(product_names)


def select_expensive_orders_2(ords):
    result = []
    for order in ords:
        if order["price"] > 500:
            result.append(order["product"])
    result.sort()
    return result

result = select_expensive_orders(orders)
result_2 = select_expensive_orders_2(orders)

print(result)
print(result == sample)
print("---")
print(result_2)
print(result_2 == sample)
