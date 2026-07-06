""" 04 Генератор тестовых данных

Создайте генератор, который
- принимает в качестве аргументов другие генераторы;
- и возвращает тюплы, состоящие из значений, полученных от каждого из них.

Используйте ранее написанные генераторы дат и имён для создания тестовых данных.

Данные:
name_gen = random_names()
date_gen = random_dates(2025)

Пример вывода:
('Emma Brown', '2025-02-14')
('Bob Williams', '2025-06-28')
('Charlie Johnson', '2025-09-09')
...
"""
from task_02 import random_dates
from task_03 import random_names

def combine_generators(*generators):
    while True:
        yield tuple(next(gen) for gen in generators)

# Используем ранее созданные генераторы
name_gen = random_names()
date_gen = random_dates(2025)

# Создаём генератор тюплов
data_gen = combine_generators(name_gen, date_gen)

# Выводим тестовые данные
for _ in range(5):
    print(next(data_gen))
