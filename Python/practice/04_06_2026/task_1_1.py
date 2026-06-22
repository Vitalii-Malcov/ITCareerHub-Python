""" 01 Сортировка по возрасту

Отсортируйте этот двумерный массив (имя, возраст) по возрасту по возрастанию.

Данные:
people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]
Пример вывода:

[('Mike', 19), ('Isabella', 19), ('Henry', 19), ('Bob', 20), ('Charlie', 23), ('Jack', 24), ('Alice', 25), ('Grace', 27), ('Kevin', 28), ('Eve', 29), ('Diana', 30), ('Laura', 31), ('Oscar', 33), ('Frank', 33), ('Nancy', 35)]
"""
people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]

example_output = [('Mike', 19), ('Isabella', 19), ('Henry', 19), ('Bob', 20), ('Charlie', 23), ('Jack', 24), ('Alice', 25), ('Grace', 27), ('Kevin', 28), ('Eve', 29), ('Diana', 30), ('Laura', 31), ('Oscar', 33), ('Frank', 33), ('Nancy', 35)]

sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)
print(sorted_people == example_output)
