""" 04 Очередь задач с приоритетом
Есть очередь задач, где каждая задача имеет приоритет: "высокий", "средний", "низкий".
Реализуйте функцию, которая сортирует очередь задач таким образом, чтобы более высокий приоритет был в начале очереди.
Нужно изменить исходную очередь, а не создавать новую.
Данные:
tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})
Пример вывода:
Очередь задач:
	task3: высокий
	task5: высокий
	task2: средний
	task1: низкий
	task4: низкий
"""
from collections import OrderedDict

tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})


def sort_by_priority(tasks):
    priority = ["низкий", "средний", "высокий"]

    for level in priority:
        for task, p in list(tasks.items()):
            if p == level:
                tasks.move_to_end(task, last=False)
sort_by_priority(tasks)

print("Очередь задач:")
for task, priority in tasks.items():
    print(f"\t{task}: {priority}")
