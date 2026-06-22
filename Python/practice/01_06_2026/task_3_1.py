""" 03 Поиск задач

Реализуйте функцию, которая
- принимает словарь задач с категориями
- и нужную категорию.

Функция должна возвращать список задач для указанной категории.

Данные:
tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"
Пример вывода:
Задачи для категории 'учёба':
['task2', 'task5']
"""

def find_tasks_by_category(tasks, category):
    result = []

    for task, cat in tasks.items():
        if cat == category:
            result.append(task)

    return result

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"
print(f"Задачи для категории '{category}':")
print(find_tasks_by_category(tasks, category))
