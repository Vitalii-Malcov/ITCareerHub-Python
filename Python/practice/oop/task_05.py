""" 05. Альтернативный конструктор

Реализуйте метод from_string(), позволяющий создавать объект из строки формата:
"Bob, 2001-12-03"

"""
from datetime import datetime

from dateutil.relativedelta import relativedelta


class Student:
    student_id = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        if self.get_age() < 16:
            raise ValueError("Студенту должно быть не менее 16 лет.")

        Student.student_id += 1
        self.student_id = Student.student_id

    def get_age(self):
        today = datetime.now().date()
        age = relativedelta(today, self.birth_date)
        return age.years

    def __repr__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def show_info(self):
        print(f"Student: \n"
            f"	Name: {self.name}\n"
            f"	Age: {self.get_age()}\n"
            f"	ID: {self.student_id}")

    @classmethod
    def from_string(cls, data: str):
        return cls(*(part.strip() for part in data.split(",")))

s1 = Student.from_string("Bob, 2001-12-03")
print(s1)

# Student: Bob, birth_date: 2001-12-03, ID: 1


