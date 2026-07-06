""" 5.2 Распределение задач

Функция task_assigner()
- читает файл tasks.txt
- и назначает задачи сотрудникам по очереди.

Она использует генератор для
- постепенного чтения новых задач
- и назначения этих задач сотрудникам.

Дополнительно: если файл tasks.txt отсутствует,
программа делает 5 попыток с паузой 3 секунды перед завершением:
Файл не найден, попытка 1/5...
Файл не найден, попытка 2/5...
Файл не найден, попытка 3/5...
Файл не найден, попытка 4/5...
Файл не найден, попытка 5/5...
Файл так и не найден. Завершаем работу.


Если же файл задач есть, то задачи распределяются между сотрудниками "по кругу":

Данные:
employees = ["Alice", "Bob", "Charlie"]

Пример вывода:
Alice выполняет: Подготовить отчёт
Bob выполняет: Провести собрание
Charlie выполняет: Проверить документацию
Alice выполняет: Разработать новый модуль
Bob выполняет: Настроить сервер
"""

import time
import itertools

MAX_ATTEMPTS = 5
RETRY_DELAY = 3
POLL_INTERVAL = 3

employees = ["Alice", "Bob", "Charlie"]
# Генератор с 5 попытками открыть файл
def task_assigner(employees, filename="tasks.txt"):
    f = None

    for attempt in range(1, MAX_ATTEMPTS +1):
        try:
            f = open(filename, "r", encoding="utf-8")
            break
        except FileNotFoundError:
            print(f'Файл не найден, попытка {attempt}/{MAX_ATTEMPTS}...')
            if attempt < MAX_ATTEMPTS:
                time.sleep(POLL_INTERVAL)

    if f is None:
        print("Файл так и не найден. Завершаем работу.")
        return

    employee_cycle = itertools.cycle(employees)

    try:
        while True:
            line = f.readline()

            if line:
                task = line.strip()
                if not task:
                    continue
                employee = next(employee_cycle)
                yield employee, task
            else:
                time.sleep(POLL_INTERVAL)
    finally:
        f.close()


if __name__ == "__main__":
    # Запуск генератора
    employees = ["Alice", "Bob", "Charlie"]
    task_generator = task_assigner(employees)

    for task in task_generator:
        employee, task = task
        print(f"{employee} выполняет: {task}")
