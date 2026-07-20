""" 03 Добавьте строковое представление объекта.

Пример вывода:
Student: Alice, birth_date: 2005-05-10, ID: 1
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

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

s1 = Student("Alice", "2005-05-10")
print(s1)
print(str(s1) == "Student: Alice, birth_date: 2005-05-10, ID: 1")

# "Student: Alice, birth_date: 2005-05-10, ID: 1")
# True
