""" 03 Объединение списков продуктов

Напишите функцию, которая
- принимает несколько (много) списков с названиями продуктов
- и возвращает генератор, содержащий все продукты в нижнем регистре.

Выведите содержимое генератора.

Данные:
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""


from itertools import chain

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def gen(*lists):
    return (item.lower() for item in chain.from_iterable(lists))


for product in gen(fruits, vegetables, dairy):
    print(product)
#################################################################################

def gen(*args):
    for product in chain(*args):
        yield product.lower()


result = gen(fruits, vegetables, dairy)

for item in result:
    print(item)
