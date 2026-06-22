"""02.1 *Задания со звёздочкой:
Вывести результат в таком формате

Товар          Старая цена    Новая цена
Laptop........     $1200.00      $996.00
Mouse.........       $25.00       $20.75
Keyboard......       $75.00       $62.25
Monitor.......      $200.00      $166.00
"""

# Список товаров: название и старая цена
products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 75),
    ("Monitor", 200),
]

# Процент скидки
discount = 17

# # Заголовок таблицы
# header = f"{'Товар':<14}  {'Старая цена':>9}  {'Новая цена':>9}"
#
# # Создаём разделитель из дефисов той же длины, что и заголовок
# separator = "-" * len(header)
# print(header)
# print(separator)
#
# # Распаковка: вместо product[0] и product[1] сразу получаем name и old_price
# for name, old_price in products:
#     # Считаем новую цену: вычитаем процент скидки от старой цены
#     # Например: 1200 * (1 - 17/100) = 1200 * 0.83 = 996.0
#     new_price = old_price * (1 - discount / 100)
#
#     # Дополняем название точками до 14 символов, выравниваем влево
#     name_with_dots = f"{name:.<14}"
#
#     # Собираем цены со знаком доллара как единую строку
#     old_str = f"${old_price:.2f}"
#     new_str = f"${new_price:.2f}"
#
#     # Выводим строку: имя + старая цена (выравнивание вправо на 9) + новая цена
#     print(f"{name_with_dots}  {old_str:>9}  {new_str:>9}")


# List comprehension с распаковкой: получаем новый список из трёх элементов
prices = [(name, old, old * (1 - discount / 100)) for name, old in products]

print(f"{'Товар':<14}{'Старая цена':>12}{'Новая цена':>12}")
print("-" * 38)

for name, old_price, new_price in prices:
    print(f"{name:.<14}{f'${old_price:.2f}':>12}{f'${new_price:.2f}':>12}")
