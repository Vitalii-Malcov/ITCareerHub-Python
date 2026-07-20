""" 07. Фильтрация студентов по возрасту

Реализуйте метод
filter_by_min_age(students: list[Student], min_age: int),
как способ отобрать из списка студентов только тех, кто старше определённого возраста.

"""
from pprint import pprint

""" 07. Фильтрация студентов по возрасту """

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Student:
    student_id = 0

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

        if self.get_age() < 16:
            raise ValueError("Student must be at least 16 years old.")

        Student.student_id += 1
        self.student_id = Student.student_id

    def get_age(self):
        return self.calculate_age_on(datetime.now().date())

    def calculate_age_on(self, target_date):
        if isinstance(target_date, datetime):
            target_date = target_date.date()
        age = relativedelta(target_date, self.birth_date)
        return age.years

    def __repr__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def show_info(self):
        print(f"Student:\n"
              f"\tName: {self.name}\n"
              f"\tAge: {self.get_age()}\n"
              f"\tID: {self.student_id}")

    @classmethod
    def from_string(cls, data: str):
        name, birth_date = (part.strip() for part in data.split(","))
        return cls(name, birth_date)

    @staticmethod
    def filter_by_min_age(students, min_age: int):
        return [student for student in students if student.get_age() >= min_age]





s1 = Student("Alice", "2005-05-10")
s2 = Student.from_string("Bob, 2001-12-03")
s3 = Student.from_string("Bill, 2009-05-15")
students = [s1, s2, s3]

pprint(Student.filter_by_min_age(students, 20))
#
# [Student: Alice, birth_date: 2005-05-10, ID: 1,
#  Student: Bob, birth_date: 2001-12-03, ID: 2]
