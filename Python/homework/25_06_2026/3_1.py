""" 03 Комбинации одежды

Напишите функцию, которая
- принимает списки
    - типов одежды,
    - цветов
    - и размеров,
- а затем генерирует все возможные комбинации в формате "Clothe - Color - Size".

Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L

"""

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

from itertools import product


def get_product(clothes, colors, sizes):
    for clothe, color, size in product(clothes, colors, sizes):
        print(f"{clothe} - {color} - {size}")

get_product(clothes, colors, sizes)

#####################################################################

def get_product(clothes, colors, sizes):
    return (f"{clothe} - {color} - {size}" for clothe, color, size in product(clothes, colors, sizes))


for combo in get_product(clothes, colors, sizes):
    print(combo)


