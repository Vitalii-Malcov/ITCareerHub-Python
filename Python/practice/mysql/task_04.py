""" 04 Фильтрация сотрудников по зарплате
Решение (использует общий модуль hr_repository.py)
"""

from local_settings_pr import dbconfig
from hr import FilterableHRRepository

dbconfig['database'] = 'hr'


def main():
    # FilterableHRRepository наследует всё от HRRepository и добавляет filter_by_salary()
    with FilterableHRRepository(dbconfig) as hr:
        hr.print_departments()

        number = int(input("Enter department number: "))
        department_name = hr.department_name_by_number(number)
        print(f"You selected: {department_name}")

        employees = hr.get_employees(department_name)

        if not employees:
            print(f"No employees found in {department_name} department.")
            return

        answer = input("Would you like to filter employees by salary? (y/n) ").strip().lower()

        if answer == 'y':
            condition = input("Enter condition (>, <, =, >=, <=): ").strip()
            value = float(input("Enter salary: "))
            employees = hr.filter_by_salary(employees, condition, value)

        hr.print_employees(department_name, employees=employees)


if __name__ == "__main__":
    main()
