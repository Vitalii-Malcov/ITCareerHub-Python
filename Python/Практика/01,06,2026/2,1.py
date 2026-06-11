"""02 Группировка задач по категории
Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
Данные:
tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
Пример вывода:
Группировка по категориям:
{
    'работа': ['task1', 'task4'],
    'учёба': ['task2', 'task5'],
    'развлечения': ['task3']
}
"""

from collections import defaultdict


def group_tasks_by_category(tasks):

    result = defaultdict(list)

    for task, category in tasks.items():
        result[category].append(task)

    return dict(result)


tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}

sample = {
    'работа': ['task1', 'task4'],
    'учёба': ['task2', 'task5'],
    'развлечения': ['task3']
}
result = group_tasks_by_category(tasks)

print(result)
print(result == sample)
