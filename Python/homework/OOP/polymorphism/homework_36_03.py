""" 03 Класс Teacher и список людей

На основе класса Person создайте класс Teacher.
- У преподавателя есть имя и предмет.
- Метод introduce() должен выводить имя и предмет.

Метод introduce() должен выводить строку:
    Hello, I am professor <имя>. My subject is <предмет>.

Создайте список, в котором будут Student и Teacher,
и вызовите у всех метод introduce().

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob.
My subject is Mathematics
"""

""" 03 Класс Teacher и список людей — 4 варианта реализации """

from abc import ABC, abstractmethod

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}")


def variant_1():
    student1 = Student("Alice", 2)
    teacher1 = Teacher("Bob", "Mathematics")
    people = [student1, teacher1]

    for person in people:
        person.introduce()
#########################################################################

class Person2:
    def __init__(self, name):
        self.name = name

class Student2(Person2):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

class Teacher2(Person2):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


def introduce_person(person):
    if isinstance(person, Student2):
        print(f"Hello, my name is {person.name}.")
        print(f"I'm on course {person.course}.")
    elif isinstance(person, Teacher2):
        print(f"Hello, I am professor {person.name}.")
        print(f"My subject is {person.subject}")


def variant_2():
    student1 = Student2("Alice", 2)
    teacher1 = Teacher2("Bob", "Mathematics")
    for person in [student1, teacher1]:
        introduce_person(person)

############################################################################
class PersonABC(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def introduce(self):
        pass  # у Person нет своей реализации — только объявление


class Student3(PersonABC):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I'm on course {self.course}.")


class Teacher3(PersonABC):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.")
        print(f"My subject is {self.subject}")


def variant_3():
    student1 = Student3("Alice", 2)
    teacher1 = Teacher3("Bob", "Mathematics")
    people = [student1, teacher1]

    for person in people:
        person.introduce()

####################################################################

def variant_4():
    student1 = Student("Alice", 2)
    student2 = Student("Kate", 3)
    teacher1 = Teacher("Bob", "Mathematics")

    people = [student1, teacher1, student2]

    students = [p for p in people if isinstance(p, Student)]
    teachers = [p for p in people if isinstance(p, Teacher)]

    for person in students + teachers:
        person.introduce()


if __name__ == "__main__":
    print("=== Вариант 1: super() ===")
    variant_1()

    print("\n=== Вариант 2: isinstance-функция ===")
    variant_2()

    print("\n=== Вариант 3: ABC ===")
    variant_3()

    print("\n=== Вариант 4: группировка списка ===")
    variant_4()
