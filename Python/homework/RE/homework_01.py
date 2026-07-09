"""Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."


Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022

"""
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

import re

pattern = r"\d{2}([/.-])\d{2}\1\d{4}"
dates = [match.group() for match in re.finditer(pattern, text)]

pattern1 = r"\d{2}([/.-])\d{2}\1\d{4}"
dates1 = [m.group() for m in re.finditer(pattern1, text)]

pattern2 = r"\d{2}[/.-]\d{2}[/.-]\d{4}"
dates2 = re.findall(pattern2, text)

pattern3 = r"(?P<day>\d{2})(?P<sep>[/.-])(?P<month>\d{2})(?P=sep)(?P<year>\d{4})"
dates3 = [m.group() for m in re.finditer(pattern3, text)]

for d, d1, d2, d3 in zip(dates, dates1, dates2, dates3):
    print(d, d1, d2, d3)




