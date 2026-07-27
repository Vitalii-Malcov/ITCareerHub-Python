""" 01 Банковский счёт — 3 варианта решения """


# одинарное подчёркивание (соглашение "protected")

class BankAccountV1:
    def __init__(self, owner, balance):
        self.owner = owner          # имя владельца — можно оставить открытым
        self._balance = balance     # баланс — "защищённый", трогать снаружи не стоит

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self._balance:
            print("Error: Not enough funds.")
            return
        self._balance -= amount

    def show_balance(self):
        print(f"Current balance: {self._balance}")



# ============================================================
# двойное подчёркивание (name mangling) + @property

class BankAccountV2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # приватный атрибут (name mangling)

    @property
    def balance(self):
        # только чтение — сеттера нет, значит balance = 100 снаружи вызовет AttributeError
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")


# ============================================================
class BankAccountV3:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __is_valid_amount(self, amount):
        # приватный метод — вспомогательная проверка, снаружи не нужна и не видна
        if amount < 0:
            print("Error: Amount must be positive.")
            return False
        return True

    def deposit(self, amount):
        if not self.__is_valid_amount(amount):
            return
        self.__balance += amount

    def withdraw(self, amount):
        if not self.__is_valid_amount(amount):
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

# Здесь вся проверка суммы вынесена в один приватный helper-метод,
# чтобы не дублировать код в deposit/withdraw.


# ============================================================
# __slots__ — экономим память и дополнительно
# запрещаем случайно создать новый атрибут снаружи

class BankAccountV4:
    __slots__ = ("owner", "_BankAccountV4__balance")

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")



# ============================================================
# Отличие от V2/V3: здесь есть сеттер для balance — вся валидация
# суммы централизована в одном месте (balance.setter), а deposit
# и withdraw просто вычисляют новое значение и присваивают его.

class BankAccountV5:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_value):
        # если кто-то снаружи попробует account.balance = -100,
        # значение молча не изменится — тоже способ защиты
        if new_value < 0:
            print("Error: balance cannot be negative.")
            return
        self.__balance = new_value

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.balance = self.__balance + amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.balance = self.__balance - amount

    def show_balance(self):
        print(f"Current balance: {self.__balance}")



# ============================================================
class PositiveAmount:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Amount must be positive.")
        setattr(obj, self._name, value)


class BankAccountV6:
    balance = PositiveAmount()  # дескриптор следит за корректностью баланса

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.balance:
            print("Error: Not enough funds.")
            return
        self.balance = self.balance - amount

    def show_balance(self):
        print(f"Current balance: {self.balance}")


def _run_demo(cls):
    print(f"--- {cls.__name__} ---")
    account = cls("Alice", 150)

    account.show_balance()
    account.deposit(-50)
    account.show_balance()
    account.withdraw(200)
    account.show_balance()
    account.deposit(100)
    account.show_balance()
    account.withdraw(50)
    account.show_balance()
    print()


if __name__ == "__main__":
    for cls in (BankAccountV1, BankAccountV2, BankAccountV3,
                BankAccountV4, BankAccountV5, BankAccountV6):
        _run_demo(cls)

# Current balance: 150
# Error: Amount must be positive.
# Current balance: 150
# Error: Not enough funds.
# Current balance: 150
# Current balance: 250
# Current balance: 200
