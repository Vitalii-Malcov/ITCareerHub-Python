""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

""" 01 Среднее время выполнения — варианты решения

Несколько разных способов реализовать декоратор measure_time.
"""

""" 01 Среднее время выполнения — варианты решения

Несколько разных способов реализовать декоратор measure_time.
Применение — через обычный синтаксис @decorator, как и положено.
"""

import time
import functools
import statistics
import timeit


def measure_time_v1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        durations = []
        result = None

        for _ in range(5):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            durations.append(end - start)

        average = sum(durations) / len(durations)
        print(f"Среднее время выполнения для 5 вызовов: {average:.2f} секунд")
        print(f"Результат: {result}")
        return result

    return wrapper


@measure_time_v1
def compute_v1():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


def measure_time_v2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        total_time = 0.0
        result = None

        for _ in range(5):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            total_time += time.perf_counter() - start

        average = total_time / 5
        print(f"Среднее время выполнения для 5 вызовов: {average:.2f} секунд")
        print(f"Результат: {result}")
        return result

    return wrapper


@measure_time_v2
def compute_v2():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


def measure_time_v3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = None

        def run_once():
            nonlocal result
            start = time.perf_counter()
            result = func(*args, **kwargs)
            return time.perf_counter() - start

        durations = [run_once() for _ in range(5)]
        average = statistics.mean(durations)

        print(f"Среднее время выполнения для 5 вызовов: {average:.2f} секунд")
        print(f"Результат: {result}")
        return result

    return wrapper


@measure_time_v3
def compute_v3():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


def measure_time(runs=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            durations = []
            result = None

            for _ in range(runs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                durations.append(time.perf_counter() - start)

            average = sum(durations) / len(durations)
            print(f"Среднее время выполнения для {runs} вызовов: {average:.2f} секунд")
            print(f"Результат: {result}")
            return result

        return wrapper

    return decorator


@measure_time(runs=3)
def compute_v4():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


def measure_time_v5(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # отдельный вызов, чтобы получить результат
        total_time = timeit.timeit(lambda: func(*args, **kwargs), number=5)
        average = total_time / 5

        print(f"Среднее время выполнения для 5 вызовов: {average:.2f} секунд")
        print(f"Результат: {result}")
        return result

    return wrapper


@measure_time_v5
def compute_v5():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


# ---------------------------------------------------------------------------
# Демонстрация — просто вызываем задекорированные функции
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("--- Вариант 1 ---")
    compute_v1()

    print("\n--- Вариант 2 ---")
    compute_v2()

    print("\n--- Вариант 3 ---")
    compute_v3()

    print("\n--- Вариант 4 (декоратор с параметром, 3 запуска) ---")
    compute_v4()

    print("\n--- Вариант 5 (через timeit) ---")
    compute_v5()
