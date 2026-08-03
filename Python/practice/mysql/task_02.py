""" 02 Выбор департамента по номеру
Решение (использует общий модуль hr_repository.py)
"""

from local_settings_pr import dbconfig
from hr import HRRepository

dbconfig['database'] = 'hr'


def main():
    # department_name_by_number() уже есть в базовом классе — подкласс здесь не нужен
    with HRRepository(dbconfig) as hr:
        hr.print_departments()

        number = int(input("Enter department number: "))
        department_name = hr.department_name_by_number(number)
        print(f"You choose: {department_name}")

        hr.print_employees(department_name)


if __name__ == "__main__":
    main()
