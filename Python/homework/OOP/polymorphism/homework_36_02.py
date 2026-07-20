""" 02 Класс Student

На основе класса Person создайте класс Student.
- Студент должен иметь имя и номер курса.
- Метод introduce() должен
    - сначала выводить базовое приветствие,
    - а затем строку: I'm on course <номер_курса>.

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
"""

from dataclasses import dataclass

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")



class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)   # не дублирую self.name = name
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")



class StudentExplicit(Person):
    def __init__(self, name, course):
        Person.__init__(self, name)  # явный вызов конструктора родителя
        self.course = course

    def introduce(self):
        Person.introduce(self)       # явный вызов метода родителя
        print(f"I'm on course {self.course}.")



@dataclass
class PersonDataclass:
    name: str

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


@dataclass
class StudentDataclass(PersonDataclass):
    course: int = 0  # поля со значением по умолчанию — после обязательных

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")



class StudentComposition:
    def __init__(self, name, course):
        self.person = Person(name)  # Person как атрибут, а не родитель
        self.course = course

    def introduce(self):
        self.person.introduce()
        print(f"I'm on course {self.course}.")


if __name__ == "__main__":
    Student("Alice", 2).introduce()
    print("---")
    StudentExplicit("Alice", 2).introduce()
    print("---")
    StudentDataclass("Alice", 2).introduce()
    print("---")
    StudentComposition("Alice", 2).introduce()

    # Все варианты дают одинаковый вывод:
    # Hello, my name is Alice.
    # I'm on course 2.



