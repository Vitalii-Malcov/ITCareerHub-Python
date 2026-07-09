import string
from itertools import permutations

# Таблица символов: ЗАГЛАВНЫЕ, затем строчные, затем цифры.
# Порядок важен: по нему идёт генерация (поэтому файл начинается с ACa0)
# и по нему же определяется, какие символы стоят "подряд".
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
    # Соседние символы пароля не должны стоять подряд в таблице CHARS.
    # Если по заданию нужно считать соседство по кодам ASCII —
    # замени POSITION[...] на ord(...).
    for i in range(len(password) - 1):
        if abs(POSITION[password[i]] - POSITION[password[i + 1]]) == 1:
            return False
    return True


def is_valid(password):
    # Условие "символы не повторяются" обеспечивает сам permutations() —
    # отдельно проверять не нужно.
    return (
        has_upper(password)
        and has_lower(password)
        and has_digit(password)
        and no_neighbors(password)
    )


def main(filename="valid_passwords.txt"):
    counter = 1
    with open(filename, "w", encoding="utf-8") as file:
        # permutations() — ленивый генератор: ~13,4 млн наборов идут по одному,
        # все сразу в памяти не держатся.
        for variant in permutations(CHARS, LENGTH):
            password = "".join(variant)
            if is_valid(password):
                file.write(f"{counter}: {password}\n")
                counter += 1
    print(f"Готово! Подходящих паролей: {counter - 1}")


if __name__ == "__main__":
    main()
