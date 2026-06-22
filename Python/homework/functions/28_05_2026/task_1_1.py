""" 01 Простое число

Напишите функцию is_prime(), которая
- проверяет, является ли число n простым (делится только на 1 и само себя)
- и возвращает булев результат.


Пример проверки функции is_prime():

chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым
"""

def is_prime(n):
    """Проверяет, является ли число n простым. Возвращает True или False."""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def chack_func_is_prime(n):
    """Печатает сообщение о том, является ли число n простым."""
    if is_prime(n):
        print(f"Число {n} является простым")
    else:
        print(f"Число {n} НЕ является простым")

chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым


def is_prime(n):
    """Проверяет, является ли число n простым. Возвращает True или False."""
    if n < 2:
        return False
    divisors = [i for i in range(2, n) if n % i == 0]
    return len(divisors) == 0


def chack_func_is_prime(n):
    """Печатает сообщение о том, является ли число n простым."""
    if is_prime(n):
        print(f"Число {n} является простым")
    else:
        print(f"Число {n} НЕ является простым")

chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым
