"""
5. Журнал вызовов функции

Создайте декоратор log_to_file, который будет записывать в файл
все вызовы функции с её аргументами и результатом.
Лог сохраняется в файл call_log.log, каждый вызов — на новой строке.

Пример применения:
@log_to_file
def add(a, b):
    return a + b

@log_to_file
def greet_with_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

@log_to_file
def greet():
    return "Hello"


Пример вывода (файл call_log.log):
2026-07-14 00:27:27,088 - INFO - function add | args 5, 3; kwargs: None | return 8
2026-07-14 00:27:27,088 - INFO - function greet_with_name | args Alice; kwargs: punctuation='.' | return Hello, Alice.
2026-07-14 00:27:27,088 - INFO - function greet | args None; kwargs: None | return Hello
"""
import functools
import logging

handlers = [
    logging.FileHandler('call_log.log'),
    logging.StreamHandler(),
]

logging.basicConfig(
    handlers=handlers,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


def log_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ', '.join(str(arg) for arg in args) if args else 'None'
        kwargs_str = ', '.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else 'None'
        logging.info(f"function {func.__name__} | args {args_str}; kwargs: {kwargs_str} | return {result}")
        return result

    return wrapper


@log_to_file
def add(a, b):
    return a + b

@log_to_file
def greet_with_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

@log_to_file
def greet():
    return "Hello"


add(5, 3)
greet_with_name("Alice", punctuation=".")
greet()

# 2026-07-14 00:27:27,088 - INFO - function add | args 5, 3; kwargs: None | return 8
# 2026-07-14 00:27:27,088 - INFO - function greet_with_name | args Alice; kwargs: punctuation='.' | return Hello, Alice.
# 2026-07-14 00:27:27,088 - INFO - function greet | args None; kwargs: None | return Hello
