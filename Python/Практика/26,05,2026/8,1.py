""" 08 Рецепты по ингредиентам

Создайте словарь, в котором
- для каждого набора ингредиентов будут храниться все названия рецептов.

Учитывайте что ингредиенты могут быть перечислены в произвольном порядке и некоторые рецепты могут иметь одинаковые ингредиенты.
Выведите возможные рецепты для каждого набора продуктов.

В конце пользователь вводит список имеющихся у него ингредиентов через пробел,
и программа должна вывести названия всех доступных рецептов.

Если рецептов нет, нужно вывести сообщение "Нет рецептов".
Данные:
recipes = {
    ("flour", "egg", "milk"): "Pancakes",
    ("egg", "milk", "butter"): "Omelette",
    ("flour", "sugar", "butter"): "Cookies",
    ("flour", "egg", "butter", "sugar"): "Cake",
    ("milk", "flour", "egg"): "Waffles",
    ("butter", "milk", "egg"): "Scrambled Eggs",
    ("flour", "milk", "sugar", "butter"): "Sweet Bread"
}

Пример ввода:
milk egg butter flour

Пример вывода:
Ингредиенты                    | Рецепты
------------------------------------------------------------
flour, milk, egg               | Pancakes, Waffles
butter, milk, egg              | Omelette, Scrambled Eggs
flour, sugar, butter           | Cookies
flour, sugar, butter, egg      | Cake
flour, sugar, butter, milk     | Sweet Bread

Введите ингредиенты через пробел: milk egg butter flour
Доступные рецепты: Pancakes, Waffles, Omelette, Scrambled Eggs
"""
from pandas.core.ops.docstrings import key

recipes = {
    ("flour", "egg", "milk"): "Pancakes",
    ("egg", "milk", "butter"): "Omelette",
    ("flour", "sugar", "butter"): "Cookies",
    ("flour", "egg", "butter", "sugar"): "Cake",
    ("milk", "flour", "egg"): "Waffles",
    ("butter", "milk", "egg"): "Scrambled Eggs",
    ("flour", "milk", "sugar", "butter"): "Sweet Bread"
}

groupes = {}

for ingred, recipes in recipes.items():
    key = frozenset(ingred)
    if key not in groupes:
        groupes[key] = []
    groupes[key].append(recipes)

for ingred, recipes_list in groupes.items():
    ingred_str = ','.join(ingred)
    recipes_str = ', '.join(recipes_list)
    print(f"{ingred_str:30} | {recipes_str}")

user_ingre = set(input('Введите ингредиенты через пробел: ').split())
available_recipes = []
for ingred, recipes_list in groupes.items():
    if ingred.issubset(user_ingre):
        available_recipes.extend(recipes_list)

if available_recipes:
    print("Доступные рецепты:", ', '.join(available_recipes))
else:
    print("Нет рецептов")
