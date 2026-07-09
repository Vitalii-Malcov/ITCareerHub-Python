""" 04 Извлечение номеров банковских карт

Реализуйте программу, которая должна
- найти все номера карт,
    - записанные как 16 цифр,
    - разделённые блоками по 4 цифры
        - пробелами,
        - дефисами
        - или без разделителей.


text = '''
Valid less_46__Testing:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456

Invalid less_46__Testing:
123456781234567
1234/5678/9012/3456
1234 5678 9012
1234-5678-ABCD-3456
1234--5678--9012--3456
1234 56789 012 3456
'''

Пример вывода:
Валидные номера:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456

"""
import re

text = """
Valid less_46__Testing:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456

Invalid less_46__Testing:
123456781234567
1234/5678/9012/3456
1234 5678 9012
1234-5678-ABCD-3456
1234--5678--9012--3456
1234 56789 012 3456
"""

def is_valid_card(line: str) -> bool:
    digits = re.sub(r'[ -]', '', line)          # убираем разрешённые разделители
    if not digits.isdigit() or len(digits) != 16:
        return False
    # проверяем, что блоки между разделителями (если есть) — по 4 цифры
    blocks = re.split(r'[ -]', line)
    if len(blocks) == 1:
        return True  # без разделителей вообще
    return all(len(b) == 4 and b.isdigit() for b in blocks)

print("Валидные номера:")
for line in text.strip().splitlines():
    line = line.strip()
    if is_valid_card(line):
        print(line)

#////////////////////////////////////////////////////
print()

card_pattern = re.compile(r'(?<!\d)\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}(?!\d)')

valid_numbers = card_pattern.findall(text)

print("Валидные номера:")
for number in valid_numbers:
    print(number)

