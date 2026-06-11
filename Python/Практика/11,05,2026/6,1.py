""" 06 Покупки с лимитом бюджета

Дан список покупок, где каждый элемент — это тюпл: (товар, цена).
Покупки распределены по приоритетности.
Пользователь вводит бюджет.
Программа должна вывести:
- список покупок, которые он может себе позволить;
- итоговую стоимость этих товаров.

Данные:
shopping_list = [
    ("Bread", 1.20),
    ("Milk", 0.99),
    ("Eggs", 2.50),
    ("Butter", 3.75),
    ("Cheese", 4.10),
    ("Apple", 0.50)
]

Пример вывода:
Введите ваш бюджет: 7

Покупки в рамках бюджета:
Bread: $1.20
Milk: $0.99
Eggs: $2.50
Apple: $0.50

Итоговая стоимость: $5.19
"""

shopping_list = [
    ("Bread", 1.20),
    ("Milk", 0.99),
    ("Eggs", 2.50),
    ("Butter", 3.75),
    ("Cheese", 4.10),
    ("Apple", 0.50)
]

budget = 7

duble = []
total_cost = 0

for item, price in shopping_list:
    if total_cost + price <= budget:
        duble.append((item, price))
        total_cost += price

print("\nПокупки в рамках бюджета:")
for item, price in duble:
    print(f"{item}: ${price:.2f}")
print(f'\n Итоговая стоимость : ${total_cost:.2f}')

