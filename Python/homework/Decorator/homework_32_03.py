""" 03. Рамка вокруг вывода

Создайте декоратор frame, который
- оборачивает результат функции рамкой из 50 символов -,
     выводя по строке до и после вызова функции.

Пример декорируемой функции:
def say_hello():
    print("Привет, игрок!")
Пример вывода:
--------------------------------------------------
Привет, игрок!
--------------------------------------------------
"""

""" 03. Рамка вокруг вывода — альтернативные варианты решения """
from contextlib import contextmanager
from functools import wraps
from typing import Callable


def frame_v1(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 50)
        result = func(*args, **kwargs)
        print("-" * 50)
        return result

    return wrapper


def frame_v2(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("-" * 50)
        result = func(*args, **kwargs)
        print("-" * 50)
        return result

    return wrapper


def frame_v3(char: str = "-", length: int = 50) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(char * length)
            result = func(*args, **kwargs)
            print(char * length)
            return result

        return wrapper

    return decorator


if __name__ == "__main__":
    print("--- v1 (базовый, @wraps) ---")

    @frame_v1
    def say_hello_v1():
        print("Привет, игрок!")

    say_hello_v1()
    print()

    print("--- v2 (без @wraps) ---")

    @frame_v2
    def say_hello_v2():
        print("Привет, игрок!")

    say_hello_v2()
    print("__name__ после декорирования:", say_hello_v2.__name__)
    print()

    print("--- v3 (параметризованный, '=' и длина 30) ---")

    @frame_v3(char="=", length=30)
    def say_hello_v3():
        print("Привет, игрок!")

    say_hello_v3()
    print()


