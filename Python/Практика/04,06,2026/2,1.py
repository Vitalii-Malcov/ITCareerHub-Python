""" 02 Сортировка по возрасту и имени

Отсортируйте двумерный массив (имя, возраст) по убыванию возраста,
в рамках одинакового возраста отсортируйте также по имени по алфавиту.
Данные:
people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]
Пример вывода:
[('Nancy', 35), ('Frank', 33), ('Oscar', 33), ('Laura', 31), ('Diana', 30), ('Eve', 29), ('Kevin', 28), ('Grace', 27), ('Alice', 25), ('Jack', 24), ('Charlie', 23), ('Bob', 20), ('Henry', 19), ('Isabella', 19), ('Mike', 19)]
"""

people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]

example_output = [('Nancy', 35), ('Frank', 33), ('Oscar', 33), ('Laura', 31), ('Diana', 30), ('Eve', 29), ('Kevin', 28), ('Grace', 27), ('Alice', 25), ('Jack', 24), ('Charlie', 23), ('Bob', 20), ('Henry', 19), ('Isabella', 19), ('Mike', 19)]

sorted_people = sorted(people, key=lambda person: (-person[1], -ord(person[0][0])))

print(sorted_people)
print(sorted_people == example_output)

