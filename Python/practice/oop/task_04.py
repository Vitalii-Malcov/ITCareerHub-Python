""" 4. Карточка студента

Добавьте метод show_info(), который выводит информацию о студенте на текущий момент.
Возраст вычисляется автоматически на основе даты рождения.

Пример вывода:
Student:
	Name: Alice
	Age: 19
	ID: 1

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

    def show_info(self):
        print(f"Student: \n"
            f"	Name: {self.name}\n"
            f"	Age: {self.get_age()}\n"
            f"	ID: {self.student_id}")

# Перерасчёт даты рождения от сегодняшней даты, чтобы Алисе всегда было 19
alis_birthday = (datetime.today() - relativedelta(years=19)).date().__str__()  #2006-12-07"

s1 = Student("Alice", alis_birthday)
s1.show_info()

# Student:
#     Name: Alice
#     Age: 19
#     ID: 1

