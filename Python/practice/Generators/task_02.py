""" 02 Генератор случайных дат

Создайте генератор, который
- генерирует случайные даты в пределах одного года.

Генератор должен
- принимать год в качестве аргумента
- и выдавать следующую случайную дату при каждом вызове, учитывая
    - количество дней в месяце,
    - а также високосные годы.

Пример вывода:
2025-11-04
2025-01-24
2025-05-08
2025-04-05
2025-12-04
"""

import random

random.seed(42)

def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def random_dates(year: int):
    days_in_month = [31, 29 if is_leap(year) else 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

    while True:
        month = random.randint(1, 12)
        day = random.randint(1, days_in_month[month - 1])
        yield f"{year:04d}-{month:02d}-{day:02d}"


if __name__ == "__main__":
    gen = random_dates(2025)

    for _ in range(5):
        print(next(gen))


# import random
# from datetime import date, timedelta
#
#
# def random_date_generator(year: int):
#     start = date(year, 1, 1)
#     end = date(year, 12, 31)
#     days_in_year = (end - start).days  # число дней в году (учитывает високосный год через разницу дат)
#
#     while True:
#         random_day = random.randint(0, days_in_year)
#         yield start + timedelta(days=random_day)
#
#
# if __name__ == "__main__":
#     gen = random_date_generator(2025)
#     for _ in range(5):
#         print(next(gen))
