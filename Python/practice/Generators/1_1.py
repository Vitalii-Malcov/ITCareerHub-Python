""" 01. Генератор, аналогичный range()

Создайте генератор custom_range(), который
- повторяет функциональность range(),
- принимая start, stop, step
- и возвращая последовательность чисел.

Данные:
custom_range(2, 10, 2)
Пример вывода:
2 4 6 8

Данные:
custom_range(10, 0, -3)
Пример вывода:
10 7 4 1
"""

# def custom_range(start, stop=None, step=1):
#     # Если передано только одно значение — это stop
#     if step == 0:
#         raise ValueError("step неможет быть = 0")
#
#     # Движение вперёд (step > 0)
#     current = start
#     if step > 0:
#         while current < stop:
#             yield current
#             current += step
#
#     # Движение назад (step <>> 0)
#     else:
#         while current > stop:
#             yield current
#             current += step
#
#
# for num in custom_range(2, 10, 2):
#     print(num, end=" ")
#
#
# print("\n==============================")
#
# for num in custom_range(10, 0, -3):
#     print(num, end=" ")


# def custom_range(start, stop, step=1):
#     if step == 0:
#         raise ValueError("step не может быть равен 0")
#
#     n = -(-(stop - start) // step)
#     n = max(n, 0)
#
#     return (start + i * step for i in range(n))
#
#
# print(*custom_range(2, 10, 2))   # 2 4 6 8
# print(*custom_range(10, 0, -3))  # 10 7 4 1


def custom_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step не может быть равен 0")
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return
    yield start
    yield from custom_range(start + step, stop, step)


print(*custom_range(2, 10, 2))
# start = 2   > yield 2
# start = 4   > yield 4
# start = 6   > yield 6
# start = 8   > yield 8
# start = 10  > stop, потому что start >= stop


print(*custom_range(10, 0, -3))
# start = 10  > yield 10
# start = 7   > yield 7
# start = 4   > yield 4
# start = 1   > yield 1
# start = -2  > stop, потому что start <= stop


