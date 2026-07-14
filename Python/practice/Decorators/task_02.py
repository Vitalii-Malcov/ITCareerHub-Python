"""
2. Ограничение с указанием длины строки

Доработайте декоратор limit_output, чтобы он принимал параметр
max_len — максимальная длина строки.

Пример применения:
@limit_output(26)
def get_text():
    return "Это очень длинный текст, который нужно обрезать."

Пример вывода:
Это очень длинный текст...
"""

import functools
def limit_output(max_len=20):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) > max_len:
                result = result[:max_len - 3] + '...'
            return result
        return wrapper
    return decorator


@limit_output(26)
def get_text():
    return "Это очень длинный текст, который нужно обрезать."


print(get_text())

# Это очень длинный текст...
