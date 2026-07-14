"""
4. Кеш с ограничением по размеру
Доработайте декоратор cache, чтобы он:
 - Принимал параметр max_size, ограничивающий количество сохранённых записей.
 - При превышении max_size — удалял самую старую запись из кеша.

Пример применения:
@cache(max_size=2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

Пример вывода:
print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

Вычисляем 2 * 3:
6
Результат из кеша:
6
Вычисляем 4 * 5:
20
Вычисляем 6 * 7:
42
Вычисляем 2 * 3:
6
"""
from collections import OrderedDict


def cache(max_size=10):
    def decorator(func):
        storage = OrderedDict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in storage:
                print('Результат из кеша:')
                return storage[key]
            else:
                result = func(*args, **kwargs)
                storage[key] = result
                if len(storage) > max_size:
                    storage.popitem(last=False)
                return result

        return wrapper

    return decorator

@cache(max_size=2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b


print(multiply(2, 3))
print(multiply(2, 3))
print(multiply(4, 5))
print(multiply(2, 3))

# Вычисляем 2 * 3:
# 6
# Результат из кеша:
# 6
# Вычисляем 4 * 5:
# 20
# Результат из кеша:
# 6
