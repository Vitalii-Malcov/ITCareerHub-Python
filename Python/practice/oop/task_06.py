""" 06. Возраст на конкретную дату

Добавьте метод calculate_age_on(target_date: datetime), который позволяет
получить возраст студента на переданную дату.

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

    def calculate_age_on(self, target_date):
        if isinstance(target_date, datetime):
            target_date = target_date.date()

        age = relativedelta(target_date, self.birth_date)
        return age.years

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def show_info(self):
        print(f"Student: \n"
            f"	Name: {self.name}\n"
            f"	Age: {self.get_age()}\n"
            f"	ID: {self.student_id}")

    @classmethod
    def from_string(cls, data: str):
        return cls(*(part.strip() for part in data.split(",")))



# Перерасчёт даты рождения от сегодняшней даты, чтобы Алисе всегда было 19
alis_birthday = (datetime.today() - relativedelta(years=19)).date()  #2006-12-07"

s1 = Student("Alice", str(alis_birthday))

# День рождения Алисы через 25 лет
alis_birthday_plus_25 = alis_birthday + relativedelta(years=25)

print(s1.calculate_age_on(alis_birthday_plus_25))
# 25
