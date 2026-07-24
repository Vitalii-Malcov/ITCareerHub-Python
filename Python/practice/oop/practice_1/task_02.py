"""
02. Номер студента
Каждому студенту (объекту student) должен автоматически присваиваться уникальный номер - student_id, начиная с 1.

Этот номер должен храниться в каждом объекте класса Student.
И, разумеется, у каждого студента он должен быть свой собственный.
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

        self.student_id = self._generate_id()

    @classmethod
    def _generate_id(cls):
        cls.student_id += 1
        return cls.student_id

    def get_age(self):
        today = datetime.today().date()
        return relativedelta(today, self.birth_date).years



print(Student.student_id == 0)  # True

s1 = Student("name1", "2000-01-01")
s2 = Student("name2", "2000-01-01")

print(Student.student_id == 2)  # True
print(s1.student_id == 1)
print(s2.student_id == 2)

# True
# True
# True
# True
