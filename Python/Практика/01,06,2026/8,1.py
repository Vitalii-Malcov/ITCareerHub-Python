""" 08 Очередь с LRU-кэшированием

Реализуйте функцию, которая
- поддерживает механизм LRU-кэша для очереди задач.

Функция должна принимать:
Текущую очередь задач.
Новые задачи для добавления.
Максимальный размер очереди.
Если лимит очереди превышен, удаляйте задачи, которые не использовались дольше всех.

Данные:
tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"

Пример вывода:
Очередь из 4 новых задач: ['task4', 'task1', 'task7', 'task2']
"""
from collections import OrderedDict

def lru_cache(queue, limit, *new_tasks):
    od = OrderedDict()
    for task in queue[-limit:]:
        od[task] = True
    for task in new_tasks:
        if task in od:
            od.move_to_end(task)
        else:
            od[task] = True
        if len(od) > limit:
            od.popitem(last=False)
    return list(od.keys())

tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"
tasks_limit = 4

result = lru_cache(tasks, tasks_limit, new1, new2, new3, new4)
print(f"Очередь из {tasks_limit} новых задач:", result)
