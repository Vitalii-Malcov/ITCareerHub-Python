""" 01 Генерация безопасных паролей

Программа должна сгенерировать все возможные пароли длиной 4 символа, соблюдая следующие условия:
- Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру.
- Символы не должны повторяться.
- Соседние символы не могут быть расположены подряд в таблице символов.
- Все подходящие пароли записываются в файл valid_passwords.txt в формате:
   1: ACa0
   2: ACa1
   3: ACa2
   4: ACa3

Подсказки:

1. Можно сначала получить все возможные варианты,
а затем оставить из них только те, что удовлетворяют условиям валидации.

2. Общее число всех возможных комбинаций (и валидных, и нет) более 13 миллионов.
Поэтому держать их все в памяти одновременно - КРАЙНЕ расточительно.
"""


import string
from itertools import permutations


CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits
POSITION = {ch: i for i, ch in enumerate(CHARS)}

LENGTH = 4


def has_upper(password):
    return any(ch.isupper() for ch in password)


def has_lower(password):
    return any(ch.islower() for ch in password)


def has_digit(password):
    return any(ch.isdigit() for ch in password)


def no_neighbors(password):
    for i in range(len(password) - 1):
        if abs(POSITION[password[i]] - POSITION[password[i + 1]]) == 1:
            return False
    return True


def is_valid(password):
    return (
        has_upper(password)
        and has_lower(password)
        and has_digit(password)
        and no_neighbors(password)
    )

counter = 1

with open("valid_passwords.txt", "w", encoding="utf-8") as file:
    for variant in permutations(CHARS, LENGTH):
        password = "".join(variant)

        if is_valid(password):
            file.write(f"{counter}: {password}\n")
            counter += 1

print(f"Готово! Подходящих паролей: {counter - 1}")



import string

CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 = 62
POSITION = {ch: i for i, ch in enumerate(CHARS)}
#i - ch, 0 - A, 1 - B, 2 - C

counter = 1


def is_valid(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if not (has_upper and has_lower and has_digit):
        return False

    for i in range(len(password) - 1):
        if abs(POSITION[password[i]] - POSITION[password[i + 1]]) == 1:
            return False

    return True


def generate(password):
    global counter

    if len(password) == 4:
        if is_valid(password):
            file.write(f"{counter}: {password}\n")
            counter += 1
        return

    for ch in CHARS:
        if ch not in password:
            generate(password + ch)


with open("valid_passwords.txt", "w", encoding="utf-8") as file:
    generate("")

print(f"Готово! Подходящих паролей: {counter - 1}")



