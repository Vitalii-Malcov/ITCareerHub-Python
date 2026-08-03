""" 01 Список сотрудников по убыванию зарплаты
Решение (использует общий модуль hr_repository.py)
"""

from local_settings_pr import dbconfig
from hr import HRRepository

dbconfig['database'] = 'hr'


def main():
    # для этого задания хватает базового класса — вводим название департамента вручную
    with HRRepository(dbconfig) as hr:
        hr.print_departments()
        department_name = input("Enter department: ").strip()
        hr.print_employees(department_name)


if __name__ == "__main__":
    main()
