""" 05 Повторный ввод при ошибке
Решение (использует общий модуль hr_repository.py)
"""

from local_settings_pr import dbconfig
from hr import ValidatingHRRepository

dbconfig['database'] = 'hr'


def main():
    # ValidatingHRRepository наследует и HRRepository, и FilterableHRRepository —
    # получает и фильтрацию, и retry-цикл выбора департамента "бесплатно"
    with ValidatingHRRepository(dbconfig) as hr:
        hr.print_departments()

        department_name = hr.choose_department()
        print(f"You selected: {department_name}")

        hr.print_employees(department_name)


if __name__ == "__main__":
    main()
