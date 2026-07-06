""" 01 Генератор Фибоначчи

Создайте генератор, который
- генерирует последовательность Фибоначчи бесконечно, возвращая по одному числу за раз.

Последовательность Фибоначчи — это ряд чисел, где
каждое следующее число равно сумме двух предыдущих.

Начинается с 0 и 1.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

from itertools import accumulate, chain, repeat, islice

def fibonacci_0():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_1():
    seq = accumulate(repeat(None), lambda pair, _: (pair[1], pair[0] + pair[1]), initial=(0, 1))
    return (pair[0] for pair in seq)


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


def fibonacci_2(a=0, b=1):
    yield a
    yield from fibonacci_2(b, a + b)

generators = [fibonacci_0, fibonacci_1, Fibonacci, fibonacci_2]

n = 10
for gen in generators:
    values = list(islice(gen(), n))
    print(f"{gen.__name__}: {values}")
