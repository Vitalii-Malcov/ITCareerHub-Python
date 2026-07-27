""" 02 История операций — 3 варианта решения

Главная проблема задачи: если property возвращает сам список self.__history,
то снаружи можно сделать account.history.append(...) и список изменится,
хотя formально мы дали доступ "только для чтения".
Каждый вариант ниже решает это по-своему.
"""



# ============================================================
class BankAccountV1:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        # возвращаем копию — изменение снаружи не влияет на __history
        return list(self.__history)

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

# любые изменения копии не затрагивают оригинал.


# ============================================================
class BankAccountV2:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return tuple(self.__history)  # неизменяемая последовательность

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

# tuple вообще не имеет метода .append(), поэтому "инъекция" упадёт
# с AttributeError, если попытаться её вызвать снаружи так же, как в списке.


# ============================================================
class BankAccountV3:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return list(self.__history)  # копия — оригинал защищён

    def __record(self, operation, amount):
        self.__history.append(f"{operation}: {amount}")

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__record("Deposit", amount)

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__record("Withdraw", amount)

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

# Аналогично варианту 1, но запись в историю вынесена в отдельный
# приватный метод, чтобы не дублировать f-строку в deposit/withdraw.


# ============================================================
class ReadOnlyView:
    def __init__(self, data):
        self.__data = data  # хранит ссылку на оригинальный список

    def __iter__(self):
        return iter(self.__data)

    def __getitem__(self, index):
        return self.__data[index]

    def __len__(self):
        return len(self.__data)

    def __eq__(self, other):
        return list(self.__data) == list(other)

    def __repr__(self):
        return repr(self.__data)


class BankAccountV4:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return ReadOnlyView(self.__history)  # у обёртки нет .append()

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")


# ============================================================
import copy

class BankAccountV5:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return copy.deepcopy(self.__history)

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")


# ============================================================

from collections import namedtuple

Operation = namedtuple("Operation", ["op_type", "amount"])

class BankAccountV6:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        # отдаём копию списка строковых представлений операций
        return [f"{op.op_type}: {op.amount}" for op in self.__history]

    def deposit(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        self.__balance += amount
        self.__history.append(Operation("Deposit", amount))

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Amount must be positive.")
            return
        if amount > self.__balance:
            print("Error: Not enough funds.")
            return
        self.__balance -= amount
        self.__history.append(Operation("Withdraw", amount))

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

# Каждая операция хранится не строкой, а именованным кортежем
# Operation(type, amount) — так удобнее анализировать историю

#=================================================================

def _run_demo(cls):
    print(f"--- {cls.__name__} ---")
    account = cls("Alice", 50)

    account.deposit(150)
    account.withdraw(100)
    account.show_balance()

    print("Operation history:")
    for operation in account.history:
        print("\t", operation)

    # попытка "взлома": изменяем то, что вернул history
    try:
        account.history.append('injection')
    except AttributeError:
        pass  # для варианта с tuple

    if list(account.history) != ["Deposit: 150", "Withdraw: 100"]:
        print("ВНИМАНИЕ! \nАККАУНТ ВЗЛОМАН! \nИстория операций изменена хакерами!!!")
    else:
        print("Взлом не удался — история защищена.\n")


if __name__ == "__main__":
    for cls in (BankAccountV1, BankAccountV2, BankAccountV3,
                BankAccountV4, BankAccountV5, BankAccountV6):
        _run_demo(cls)

# Current balance: 100
# Operation history:
# 	 Deposit: 150
# 	 Withdraw: 100
