""" 04 Исключение при блокировке

Доработайте класс Door:
Создайте пользовательское исключение DoorBlockedError.
При попытке открыть дверь (или сменить код) во время блокировки
выбрасывайте это исключение вместо вывода сообщения.

Обработайте исключение в коде вызова.
"""

import time
from datetime import datetime, timedelta


class DoorBlockedError(Exception):
    """Raised when trying to access a blocked door."""


class Door:
    def __init__(self, code, max_attempts=3, block_minutes=15):
        self.__code = code
        self.__max_attempts = max_attempts
        self.__block_duration = timedelta(minutes=block_minutes)
        self.__failed_attempts = 0
        self.__blocked_until = None

    def __is_valid_code(self, code):
        return code == self.__code

    def __is_blocked(self):
        if self.__blocked_until is None:
            return False
        if datetime.now() >= self.__blocked_until:
            self.__blocked_until = None
            return False
        return True

    def __remaining_block_time(self):
        remaining = self.__blocked_until - datetime.now()
        total_seconds = max(0, int(remaining.total_seconds()))
        return divmod(total_seconds, 60)

    def __check_block(self):
        if self.__is_blocked():
            minutes, seconds = self.__remaining_block_time()
            raise DoorBlockedError(f"Door is blocked. Try again in {minutes} min {seconds} sec.")


    def __register_failure(self):
        self.__failed_attempts += 1
        if self.__failed_attempts >= self.__max_attempts:
            self.__blocked_until = datetime.now() + self.__block_duration
            self.__failed_attempts = 0
            raise DoorBlockedError("Too many failed attempts.")

    def unlock(self, code):
        self.__check_block()

        if self.__is_valid_code(code):
            self.__failed_attempts = 0
            print("Access granted.")
            return True
        else:
            print("Access denied.")
            self.__register_failure()
            return False

    def change_code(self, old_code, new_code):
        self.__check_block()

        if self.__is_valid_code(old_code):
            self.__code = new_code
            self.__failed_attempts = 0
            print('Code changed.')
            return True
        else:
            print("Access denied. Code not changed.")
            self.__register_failure()
            return False




if __name__ == "__main__":
    d = Door("1234", max_attempts=2, block_minutes=0.05)

    try:
        d.unlock("1111")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.change_code("0000", "9999")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')

    time.sleep(5)

    try:
        d.unlock("1234")
    except DoorBlockedError as e:
        print(f'{e.__class__.__name__}: {e}')


# Access denied.
# Access denied. Code not changed.
# Too many failed attempts.
# DoorBlockedError: Door is blocked. Try again in 0 min 2 sec.
# Access granted.
