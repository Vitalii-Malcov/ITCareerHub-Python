""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
import time

""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
import time
import functools
import statistics


def measure_time_v1(times=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total_time = 0.0
            result = None
            for _ in range(times):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total_time += (end - start)

            avg_time = total_time / times
            print(f"Среднее время выполнения для {times} вызовов: {avg_time:.2f} секунд")
            return result
        return wrapper
    return decorator


def measure_time_v2(times=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            durations = []
            result = None

            for _ in range(times):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                finish = time.perf_counter()
                durations.append(finish - start)

            avg_time = sum(durations) / len(durations)
            print(f"Среднее время выполнения для {times} вызовов: {avg_time:.2f} секунд")
            return result
        return wrapper
    return decorator


def measure_time_v3(times=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            durations = [
                _time_single_call(func, args, kwargs)
                for _ in range(times)
            ]
            avg_time = statistics.mean(durations)
            print(f"Среднее время выполнения для {times} вызовов: {avg_time:.2f} секунд")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def _time_single_call(func, args, kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start



def measure_time_v4(func=None, *, times=10):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            total_time = 0.0
            result = None
            for _ in range(times):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                total_time += time.perf_counter() - start

            avg_time = total_time / times
            print(f"Среднее время выполнения для {times} вызовов: {avg_time:.2f} секунд")
            return result
        return wrapper

    if func is not None:
        return decorator(func)
    return decorator


def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


print("--- Вариант 1 (time.time) ---")
compute_v1 = measure_time_v1(10)(compute)
result_v1 = compute_v1()
print(f"Результат: {result_v1}\n")

print("--- Вариант 2 (perf_counter) ---")
compute_v2 = measure_time_v2(10)(compute)
result_v2 = compute_v2()
print(f"Результат: {result_v2}\n")

print("--- Вариант 3 (statistics.mean) ---")
compute_v3 = measure_time_v3(10)(compute)
result_v3 = compute_v3()
print(f"Результат: {result_v3}\n")

print("--- Вариант 4 (без лишних вызовов, поддержка без скобок) ---")
compute_v4 = measure_time_v4(times=10)(compute)
result_v4 = compute_v4()
print(f"Результат: {result_v4}\n")

@measure_time_v4
def compute_short():
    return sum(range(1_000_000))


print("--- Вариант 4 без скобок (times=10 по умолчанию) ---")
result_v4_short = compute_short()
print(f"Результат: {result_v4_short}")



###### ПРИМЕР: @measure_time_v4(times=3) ######
# ВЕТКА func=None -> используем @measure_time_v4(times=3) СО скобками
#
# СТАРТ total_time = 0.0, result = None
#
#   --- Итерация 1/3 ---
#   start        = 26.584224
#   result       = 499500   -- перезаписывается каждый раз
#   duration     = 0.000058 сек (время этого вызова)
#   total_time   = 0.000058   -- накопительная сумма
#
#   --- Итерация 2/3 ---
#   start        = 26.584338
#   result       = 499500   -- перезаписывается каждый раз
#   duration     = 0.000014 сек (время этого вызова)
#   total_time   = 0.000072   -- накопительная сумма
#
#   --- Итерация 3/3 ---
#   start        = 26.584363
#   result       = 499500
#   duration     = 0.000013 сек
#   total_time   = 0.000085
#
#   ФИНАЛ ЦИКЛА
#   avg_time = total_time / times = 0.000085 / 3 = 0.000028
#
# Среднее время выполнения для 3 вызовов: 0.00 секунд
# RETURN wrapper возвращает result = 499500
#
# >>> ЧТО ПОЛУЧИЛ СНАРУЖИ: 499500
