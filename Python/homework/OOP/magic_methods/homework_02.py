""" 02. Класс для работы с деньгами

Создайте класс Money, в котором можно:
- складывать и вычитать объекты через операторы + и -
- выводить объект как строку в виде "$<amount>"
- при сложении и вычитании возвращается новый объект
- если вычитание приводит к отрицательному значению — вернуть 0

Пример использования:
money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

Пример вывода:
$150
$50
$0
"""


class Money1:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        # Складываем суммы и возвращаем новый объект
        return Money1(self.amount + other.amount)

    def __sub__(self, other):
        # Вычитаем, но не уходим в минус
        result = self.amount - other.amount
        return Money1(max(result, 0))

    def __str__(self):
        return f"${self.amount}"


# ---------------------------------------------------------------------------
class Money2:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money2):
            return NotImplemented
        return Money2(self.amount + other.amount)

    def __sub__(self, other):
        if not isinstance(other, Money2):
            return NotImplemented
        result = self.amount - other.amount
        return Money2(result if result > 0 else 0)

    def __str__(self):
        return f"${self.amount}"

    def __repr__(self):
        return f"Money2({self.amount})"


# ---------------------------------------------------------------------------
class Money3:
    __slots__ = ("_amount",)  # экономим память, запрещаем случайные новые атрибуты

    def __init__(self, amount):
        self._amount = max(amount, 0)

    @property
    def amount(self):
        # amount доступен только для чтения снаружи
        return self._amount

    def __add__(self, other):
        return Money3(self.amount + other.amount)

    def __sub__(self, other):
        return Money3(self.amount - other.amount)  # отрицательное обнулится в __init__

    def __str__(self):
        return f"${self.amount}"


# ---------------------------------------------------------------------------
class Money4:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other ):
        return Money4(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        return Money4(max(result, 0))

    def __eq__(self, other):
        # Позволяет сравнивать money1 == money2
        return isinstance(other, Money4) and self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __str__(self):
        return f"${self.amount}"


# ---------------------------------------------------------------------------
class Money5:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money5(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        return Money5(max(result, 0))

    def __iadd__(self, other):
        # Вызывается при money1 += money2 — меняем сам объект, а не создаём новый
        self.amount += other.amount
        return self

    def __isub__(self, other):
        self.amount = max(self.amount - other.amount, 0)
        return self

    def __bool__(self):
        return self.amount > 0

    def __str__(self):
        return f"${self.amount}"


# ---------------------------------------------------------------------------
class Money6:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        # Money6 + Money6 или Money6 + int
        other_amount = other.amount if isinstance(other, Money6) else other
        return Money6(self.amount + other_amount)

    def __radd__(self, other):
        # Вызывается, когда слева обычное число: 100 + money1
        # Нужен для работы sum([money1, money2, money3])
        return self.__add__(other)

    def __sub__(self, other):
        other_amount = other.amount if isinstance(other, Money6) else other
        result = self.amount - other_amount
        return Money6(max(result, 0))

    def __str__(self):
        return f"${self.amount}"

    def __format__(self, format_spec):
        # Позволяет использовать f"{money1:.2f}" — форматируем как число
        return f"${format(self.amount, format_spec)}"


# ---------------------------------------------------------------------------
class Money7:
    def __init__(self, amount):
        self._amount = amount  # "приватный" атрибут — объект неизменяемый

    @property
    def amount(self):
        return self._amount

    def __add__(self, other):
        return Money7(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        return Money7(max(result, 0))

    def __eq__(self, other):
        return isinstance(other, Money7) and self.amount == other.amount

    def __hash__(self):
        # Без этого метода объект нельзя было бы положить в set/dict после __eq__
        return hash(self.amount)

    def __str__(self):
        return f"${self.amount}"

    def __repr__(self):
        return f"Money7({self.amount!r})"


if __name__ == "__main__":

    print("=== Вариант 1 — базовый ===")
    money1, money2 = Money1(100), Money1(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0

    print("\n=== Вариант 2 — проверка типа + __repr__ ===")
    money1, money2 = Money2(100), Money2(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0
    print(repr(money1))     # Money2(100)

    print("\n=== Вариант 3 — @property + __slots__ ===")
    money1, money2 = Money3(100), Money3(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0

    print("\n=== Вариант 4 — сравнение (__eq__, __lt__, __le__) ===")
    money1, money2 = Money4(100), Money4(50)
    print(money1 + money2)      # $150
    print(money1 - money2)      # $50
    print(money2 - money1)      # $0
    print(money1 > money2)      # True
    print(money1 == Money4(100))  # True

    print("\n=== Вариант 5 — __iadd__/__isub__ + __bool__ ===")
    money1, money2 = Money5(100), Money5(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0
    money1 += money2
    print(money1)            # $150
    empty = Money5(0)
    if not empty:
        print("Баланс пуст")

    print("\n=== Вариант 6 — __radd__ + __format__ ===")
    money1, money2 = Money6(100), Money6(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0
    total = sum([money1, money2, Money6(25)])  # работает благодаря __radd__
    print(total)              # $175
    print(f"{money1:.2f}")    # $100.00

    print("\n=== Вариант 7 — __hash__ + __repr__ ===")
    money1, money2 = Money7(100), Money7(50)
    print(money1 + money2)  # $150
    print(money1 - money2)  # $50
    print(money2 - money1)  # $0
    unique_amounts = {Money7(100), Money7(100), Money7(50)}
    print(len(unique_amounts))  # 2 — дубликаты схлопнулись благодаря __eq__/__hash__

# $150
# $50
# $0
