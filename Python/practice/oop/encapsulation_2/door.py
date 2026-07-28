"""
Door — электронная дверь с кодовым доступом.

"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Iterable, Iterator


class DoorBlockedError(Exception):
    """Raised when trying to access a blocked door."""


class Door:
    __slots__ = (
        "_code", "max_attempts", "_block_duration",
        "_failed_attempts", "_blocked_until",
    )

    def __init__(self, code: str, max_attempts: int = 3, block_minutes: float = 15):
        self._code = code
        self.max_attempts = max_attempts
        self._block_duration = timedelta(minutes=block_minutes)
        self._failed_attempts = 0
        self._blocked_until: datetime | None = None


# код доступа — только через property, снаружи никаких прямых записей
    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        if not value:
            raise ValueError("Код не может быть пустым.")
        self._code = value


    # состояние блокировки
    @property
    def is_blocked(self) -> bool:
        if self._blocked_until is None:
            return False
        if datetime.now() >= self._blocked_until:
            self._blocked_until = None      # блокировка истекла — снимаем её
            return False
        return True

    @property
    def remaining_block_time(self) -> tuple[int, int]:
        """(минуты, секунды) до конца блокировки; (0, 0), если не заблокирована."""
        if not self.is_blocked:
            return 0, 0
        seconds_left = (self._blocked_until - datetime.now()).total_seconds()
        return divmod(max(0, int(seconds_left)), 60)

    def _ensure_unblocked(self) -> None:
        if self.is_blocked:
            minutes, seconds = self.remaining_block_time
            raise DoorBlockedError(f"Door is blocked. Try again in {minutes} min {seconds} sec.")

    def _register_failure(self) -> None:
        self._failed_attempts += 1
        if self._failed_attempts >= self.max_attempts:
            self._blocked_until = datetime.now() + self._block_duration
            self._failed_attempts = 0
            print("Too many failed attempts.")


    # публичный интерфейс
    def unlock(self, code: str) -> bool:
        self._ensure_unblocked()
        success = code == self.code
        if success:
            self._failed_attempts = 0
            print("Access granted.")
        else:
            print("Access denied.")
            self._register_failure()
        return success

    def change_code(self, old_code: str, new_code: str) -> bool:
        self._ensure_unblocked()
        success = old_code == self.code
        if success:
            self.code = new_code            # проходит через сеттер с валидацией
            self._failed_attempts = 0
            print("Code changed.")
        else:
            print("Access denied. Code not changed.")
            self._register_failure()
        return success

    def attempts(self, codes: Iterable[str]) -> "DoorAttemptIterator":
        """Возвращает ленивый итератор, перебирающий codes по одному."""
        return DoorAttemptIterator(self, codes)

    def __repr__(self) -> str:
        state = "blocked" if self.is_blocked else "active"
        return f"Door(attempts={self._failed_attempts}/{self.max_attempts}, {state})"


class DoorAttemptIterator:
    """
    Итератор, вручную реализующий протокол __iter__ / __next__.
    На каждый next() пробует очередной код через door.unlock(). Останавливается
    (StopIteration) сам, если код подошёл, если коды кончились, или если дверь
    заблокировалась в процессе перебора.
    """

    def __init__(self, door: Door, codes: Iterable[str]):
        self._door = door
        self._codes: Iterator[str] = iter(codes)   # приводим любой iterable к итератору
        self._finished = False

    def __iter__(self) -> "DoorAttemptIterator":
        return self                                 # итератор возвращает сам себя

    def __next__(self) -> tuple[str, bool]:
        if self._finished:
            raise StopIteration

        code = next(self._codes)                     # штатно пробрасывает StopIteration дальше, когда коды кончились

        try:
            success = self._door.unlock(code)
        except DoorBlockedError:
            self._finished = True
            raise StopIteration                       # блокировка — тоже причина остановить перебор

        if success:
            self._finished = True                      # нашли код — следующий next() сразу даст StopIteration

        return code, success


if __name__ == "__main__":
    door = Door("1234", max_attempts=2, block_minutes=0.05)

    print("--- unlock / change_code / блокировка / исключение ---")
    try:
        door.unlock("0000")
        door.change_code("0000", "9999")     # вторая неудача -> блокировка
        door.unlock("1234")                   # дверь уже заблокирована -> исключение
    except DoorBlockedError as e:
        print(f"{e.__class__.__name__}: {e}")

    time.sleep(3.1)                            # ждём окончания блокировки
    door.unlock("1234")

    print("\n--- перебор кодов через собственный итератор ---")
    door2 = Door("7777", max_attempts=10)
    for code, success in door2.attempts(["1111", "2222", "7777", "9999"]):
        print(f"  {code} -> {'успех' if success else 'неудача'}")

    print("\n--- то же самое, но вручную через next() ---")
    door3 = Door("42", max_attempts=10)
    iterator = iter(door3.attempts(["10", "20", "42"]))
    while True:
        try:
            code, success = next(iterator)
            print(f"  {code}: {success}")
        except StopIteration:
            break

    print(f"\n{door!r}")
