"""
Door — электронная дверь с кодовым доступом, защитой от подбора кода
и временной блокировкой.
"""

from __future__ import annotations

import time
from datetime import datetime, timedelta
from typing import Iterable, Iterator


class DoorBlockedError(Exception):
    """Raised when trying to access a blocked door."""


class Door:
    def __init__(self, code: str, max_attempts: int = 3, block_minutes: float = 15):
        self._code = code
        self.max_attempts = max_attempts
        self._block_duration = timedelta(minutes=block_minutes)
        self._failed_attempts = 0
        self._blocked_until: datetime | None = None

    @property
    def code(self) -> str:
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        if not value:
            raise ValueError("Код не может быть пустым.")
        self._code = value

    @property
    def is_blocked(self) -> bool:
        if self._blocked_until is None:
            return False
        if datetime.now() >= self._blocked_until:
            self._blocked_until = None
            return False
        return True

    @property
    def remaining_block_time(self) -> tuple[int, int]:
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
            self.code = new_code
            self._failed_attempts = 0
            print("Code changed.")
        else:
            print("Access denied. Code not changed.")
            self._register_failure()
        return success

    def attempts(self, codes: Iterable[str]) -> Iterator[tuple[str, bool]]:
        """Лениво пробует каждый код; останавливается на успехе или блокировке."""
        for code in codes:
            try:
                success = self.unlock(code)
            except DoorBlockedError:
                return
            yield code, success
            if success:
                return

    def __repr__(self) -> str:
        state = "blocked" if self.is_blocked else "active"
        return f"Door(attempts={self._failed_attempts}/{self.max_attempts}, {state})"


if __name__ == "__main__":
    door = Door("1234", max_attempts=2, block_minutes=0.05)

    try:
        door.unlock("0000")
        door.change_code("0000", "9999")   # вторая неудача -> блокировка
        door.unlock("1234")                 # дверь уже заблокирована -> исключение
    except DoorBlockedError as e:
        print(f"{e.__class__.__name__}: {e}")

    time.sleep(3.1)
    door.unlock("1234")

    print()
    door2 = Door("7777", max_attempts=10)
    for code, success in door2.attempts(["1111", "2222", "7777", "9999"]):
        print(f"  {code} -> {'успех' if success else 'неудача'}")

    print(f"\n{door!r}")
