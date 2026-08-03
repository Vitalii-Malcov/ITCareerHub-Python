""" 03 Пустой департамент
Решение (использует общий модуль hr_repository.py)
"""

from local_settings_pr import dbconfig
from hr import HRRepository

dbconfig['database'] = 'hr'


def main():
    # проверка на пустой департамент уже реализована в HRRepository.print_employees() —
    # переопределять или наследовать ради неё не требуется
    with HRRepository(dbconfig) as hr:
        hr.print_departments()

        number = int(input("Enter department number: "))
        department_name = hr.department_name_by_number(number)
        print(f"You selected: {department_name}")

        hr.print_employees(department_name)


if __name__ == "__main__":
    main()
