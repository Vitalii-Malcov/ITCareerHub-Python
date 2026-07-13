""" 02 Расширяемый логгер событий

Создайте функцию, которая
- возвращает функцию "вложенный логгер событий".

Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано)
и возвращать весь список событий.

Пример вызова:
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)

Пример вывода:
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29

"""

from datetime import datetime

""" 02 Расширяемый логгер событий — альтернативные варианты решения """
from datetime import datetime
from typing import Callable, List, Optional


def make_logger_v1() -> Callable:
    events = []

    def logger(message: str = None):
        if message is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{message}: {timestamp}")
        return events

    return logger


def make_logger_v2() -> Callable:
    def logger(message: str = None):
        if message is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logger.events.append(f"{message}: {timestamp}")
        return logger.events

    logger.events = []
    return logger


def make_logger_v3() -> Callable:
    events = []

    def logger(message: str = None):
        if message is not None:
            events.append((message, datetime.now()))
        return [f"{msg}: {ts:%Y-%m-%d %H:%M:%S}" for msg, ts in events]

    return logger


def make_logger_v4() -> Callable:
    events = []
    count = 0

    def logger(message: str = None):
        nonlocal count
        if message is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"[{count}] {message}: {timestamp}")
            count += 1
        return events

    return logger


if __name__ == "__main__":
    for name, factory in [
        ("v1 (closure + list)", make_logger_v1),
        ("v2 (атрибут функции)", make_logger_v2),
        ("v3 (tuple + форматирование при выводе)", make_logger_v3),
        ("v4 (nonlocal счётчик)", make_logger_v4),
    ]:
        log = factory()
        log("Загрузка данных")
        log("Обработка завершена")
        log("Сохранение файла")
        print(f"--- {name} ---")
        for event in log():
            print(event)
