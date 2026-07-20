""" 01 Класс Person

Создайте класс Person, представляющий человека.
- Каждый человек должен иметь имя.
- Добавьте метод introduce(), который выводит приветствие с именем.

Пример вывода:
Hello, my name is Alice.
"""

""" 01 Класс Person — 4 варианта реализации """

from dataclasses import dataclass

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")



class PersonFormat:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is {}.".format(self.name))



@dataclass
class PersonDataclass:
    name: str

    def introduce(self):
        print(f"Hello, my name is {self.name}.")



class PersonStr:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello, my name is {self.name}."

    def introduce(self):
        print(self)  # переиспользуем __str__


if __name__ == "__main__":
    Person("Alice").introduce()
    PersonFormat("Alice").introduce()
    PersonDataclass("Alice").introduce()
    PersonStr("Alice").introduce()

    # Все варианты дают одинаковый вывод:
    # Hello, my name is Alice.
