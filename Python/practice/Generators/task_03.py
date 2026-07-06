""" 03 Генератор случайных имён

Создайте генератор, который
- выдаёт случайные имена и фамилии.

Выведите 5 имён.

Для получения случайного значения из списка можно
использовать choice() из модуля random.

Данные:
first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]

Пример вывода:
Alice Smith
Charlie Johnson
Bob Johnson
Alice Jones
Alice Jones
"""

from random import choice, seed
seed(42)

first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]


def random_names():
    while True:
        yield f"{choice(first_names)} {choice(last_names)}"


if __name__ == "__main__":

    gen = random_names()

    for _ in range(5):
        print(next(gen))
