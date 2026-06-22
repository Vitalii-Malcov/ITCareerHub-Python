""" 02 Статистика продаж

Дан двумерный массив продаж (список тюплов): (товар, количество, цена).

Напишите программу, которая:
- Вычисляет общую выручку для каждого товара.
- Возвращает словарь с товарами {товар: выручка},
    отсортированный по убыванию выручки.

Данные:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

"""

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

sample = {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}


def calculate_sales(sales):
    result = {}
    for product, quantity, price in sales:
        revenue = quantity * price
        result[product] = revenue

    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


result = calculate_sales(sales)
print(result)
print(str(result) == str(sample))
