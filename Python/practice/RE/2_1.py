""" 02 Поиск немецких мобильных номеров

Реализуйте программу, которая:
- находит в тексте все немецкие мобильные номера, записанные в одном из следующих форматов:
    - начинаются с +49 или 0049,
    - далее префикс мобильного оператора, начинающийся на 15, 16 или 17,
    - далее — от 7 до 9 цифр (в номере могут быть пробелы, дефисы или табуляции между блоками).

- очищает найденные номера от пробелов, дефисов, табов.
- преобразует номер в единый формат, начинающийся с +49.
- проверяет, что в результате (после очистки):
    - префикс после +49 должен начинаться с 15, 16 или 17.
    - и содержит 10–12 цифр после кода страны
                (то есть общий формат: +49XXXXXXXXXX — от 13 до 15 символов).
- возвращает список валидных номеров.

Данные (файл german_numbers.txt):
+49 157 12345678
0049-160-9876543
+49176 2345 6789
+49 89 123456                     # <- не мобильный (городской)
0049-151-456-7890
+49 178 111-22-33
+49-152-12 34 567
0044 7700 900123                  # <- Великобритания
+49160-1234-5
...
Пример вывода:
Валидные номера:
+4917623456789
+491514567890
+491781112233
+491521234567
+49154234567890
...

"""

import re
from typing import Iterator


def extract_mobile_numbers(text) -> list[str]:
    pattern = re.compile(r'(\+49|0049)[ \t\-]*(1[567]\d)[ \t\-]*((?:\d[ \t\-]*){6,8}\d)')

    valid_numbers = []

    for match in pattern.finditer(text):
        operator_code = match.group(2)
        rest = match.group(3)

        digits = re.sub(r'\D', '', operator_code + rest)
        number = f'+49{digits}'

        if 10 <= len(digits) <= 12:
            valid_numbers.append(number)
    return valid_numbers


def read_file(file_path) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

text = read_file('german_numbers.txt')
valid_numbers = extract_mobile_numbers(text)

print("Валидные номера:")
for number in valid_numbers:
    print(number)


#//////////////////////////////////////////////////////////////////////////////////
CANDIDATE_RE = re.compile(r'(?:\+49|0049)[ \t\-]*1[567][\d \t\-]{5,17}\d')

STRICT_RE = re.compile(r'^\+49(1[567]\d)(\d{7,9})$')


def normalize(raw: str) -> str:
    digits = re.sub(r'\D', '', raw)
    digits = digits.removeprefix('0049').removeprefix('49')
    return f'+49{digits}'


def extract_mobile_numbers(text: str) -> Iterator[str]:
    for raw in CANDIDATE_RE.findall(text):
        number = normalize(raw)
        if STRICT_RE.fullmatch(number):
            yield number


def read_file(path: str) -> str:
    with open(path, encoding='utf-8') as f:
        return f.read()

print()

text = read_file('german_numbers.txt')
print("Валидные номера:")
for number in extract_mobile_numbers(text):
    print(number)


