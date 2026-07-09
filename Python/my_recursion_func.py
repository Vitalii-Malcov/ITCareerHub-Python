import string

# Таблица символов: ЗАГЛАВНЫЕ, затем строчные, затем цифры.
CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits
POSITION = {ch: i for i, ch in enumerate(CHARS)}
LENGTH = 4


def is_neighbor(a, b):

    return abs(POSITION[a] - POSITION[b]) == 1


def has_all_categories(password):

    return (
        any(ch.isupper() for ch in password)
        and any(ch.islower() for ch in password)
        and any(ch.isdigit() for ch in password)
    )


def generate(prefix=""):

    if len(prefix) == LENGTH:
        if has_all_categories(prefix):
            yield prefix
        return

    for ch in CHARS:
        if ch in prefix:                              # символы не повторяются
            continue
        if prefix and is_neighbor(prefix[-1], ch):    # не соседи по таблице
            continue
        yield from generate(prefix + ch)              # спускаемся глубже


def main(filename="valid_passwords.txt"):
    counter = 1
    with open(filename, "w", encoding="utf-8") as file:
        for password in generate():
            file.write(f"{counter}: {password}\n")
            counter += 1
    print(f"Готово! Подходящих паролей: {counter - 1}")


if __name__ == "__main__":
    main()
