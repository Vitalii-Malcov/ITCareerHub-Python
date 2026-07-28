""" 03 Блокировка двери

Доработайте класс Door:
- при создании можно указать:
    - максимальное количество попыток (по умолчанию 3)
    - время блокировки в минутах (по умолчанию 15)
- если попытки исчерпаны, дверь блокируется на указанное время.
- пока дверь заблокирована — сменить код или открыть нельзя.
- неверные попытки входа (или смены кода) учитываются общим счётчиком.
- при блокировке должно выводиться сообщение с указанием оставшегося времени ожидания.
"""

import time
from datetime import datetime, timedelta

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
            print(f"Door is blocked. Try again in {minutes} minutes and {seconds} seconds.")
            return True
        return False

    def __register_failure(self):
        self.__failed_attempts += 1
        if self.__failed_attempts >= self.__max_attempts:
            self.__blocked_until = datetime.now() + self.__block_duration
            self.__failed_attempts = 0
            print('Too many  failed attempts.')

    def unlock(self, code):
        if self.__check_block():
            return False

        if self.__is_valid_code(code):
            self.__failed_attempts = 0
            print("Access granted.")
            return True
        else:
            print("Access denied.")
            self.__register_failure()
            return False

    def change_code(self, old_code, new_code):
        if self.__check_block():
            return False

        if self.__is_valid_code(old_code):
            self.__code = new_code
            self.__failed_attempts = 0
            print('Code changed.')
            return True
        else:
            print("Access denied. Code not changed.")
            self.__register_failure()
            return False



# Пример использования
d = Door("1234", max_attempts=2, block_minutes=0.05)

d.unlock("1111")
d.change_code("2222", "9999")
d.unlock("1234")
time.sleep(5)
d.unlock("1234")

