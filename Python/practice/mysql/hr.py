"""
hr_repository.py

Общий модуль для всех заданий 01–05.
Здесь собрана ВСЯ логика работы с БД hr, которая иначе дублировалась
бы в каждом файле задания. Файлы заданий импортируют отсюда нужный
класс и добавляют только то, что специфично именно для их задачи.

Иерархия классов:

    HRRepository                (базовый: соединение, департаменты, сотрудники)
        └── FilterableHRRepository   (+ фильтрация по зарплате)
                └── ValidatingHRRepository  (+ устойчивый к ошибкам выбор департамента)
"""

import operator
import mysql.connector


class HRRepository:
    """
    Базовый класс: инкапсулирует соединение, курсор и запросы,
    общие для всех заданий — получение департаментов и сотрудников.
    """

    def __init__(self, dbconfig):
        self._connection = mysql.connector.connect(**dbconfig)
        self._cursor = self._connection.cursor(dictionary=True)
        self._departments = None  # кеш, заполняется при первом обращении к departments()

    # --- протокол контекстного менеджера ---
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._connection.close()
        return False  # исключения наружу не подавляем

    # --- департаменты ---
    def departments(self):
        """Список департаментов с кешированием — запрос к БД выполняется только один раз."""
        if self._departments is None:
            self._cursor.execute("SELECT department_name FROM departments ORDER BY department_name")
            self._departments = self._cursor.fetchall()
        return self._departments

    def print_departments(self):
        for i, dept in enumerate(self.departments(), start=1):
            print(f"{i}. {dept['department_name']}")

    def department_name_by_number(self, number):
        """Переводит номер из списка (с 1) в название департамента."""
        return self.departments()[number - 1]['department_name']

    # --- сотрудники ---
    def get_employees(self, department_name):
        query = """
            SELECT e.first_name, e.last_name, j.job_title, e.salary
            FROM employees e
            JOIN departments d ON e.department_id = d.department_id
            JOIN jobs j ON e.job_id = j.job_id
            WHERE d.department_name = %s
            ORDER BY e.salary DESC
        """
        self._cursor.execute(query, (department_name,))
        return self._cursor.fetchall()

    def print_employees(self, department_name, employees=None):
        """
        Печатает сотрудников департамента.
        Если employees не передан — сам запрашивает их через get_employees().
        Если передан (например, уже отфильтрованный список из FilterableHRRepository) —
        использует его без повторного запроса к БД.
        """
        if employees is None:
            employees = self.get_employees(department_name)

        if not employees:
            print(f"No employees found in {department_name} department.")
            return

        for i, emp in enumerate(employees, start=1):
            print(f"{i}. {emp['first_name']} {emp['last_name']} — {emp['job_title']} — {emp['salary']:.2f}")


class FilterableHRRepository(HRRepository):
    """
    Наследник HRRepository — добавляет фильтрацию сотрудников по зарплате.
    Всё остальное (соединение, департаменты, базовый вывод) берёт от родителя без изменений.
    """

    # атрибут класса — общий для всех экземпляров; словарь функций сравнения
    # безопаснее, чем eval(f"{salary} {condition} {value}")
    OPERATORS = {
        '>': operator.gt,
        '<': operator.lt,
        '=': operator.eq,
        '>=': operator.ge,
        '<=': operator.le,
    }

    def filter_by_salary(self, employees, condition, value):
        """Возвращает только тех сотрудников, у кого salary удовлетворяет condition и value."""
        compare = self.OPERATORS[condition]
        return [emp for emp in employees if compare(emp['salary'], value)]


class ValidatingHRRepository(FilterableHRRepository):
    """
    Наследник FilterableHRRepository — добавляет устойчивый к ошибкам выбор департамента.
    Получает фильтрацию "бесплатно" от родителя за счёт наследования.
    """

    def choose_department(self):
        """Запрашивает номер департамента, пока не получит корректный."""
        departments = self.departments()

        while True:
            raw = input("Enter department number: ").strip()

            if not raw.isdigit():
                print("Invalid input. Please enter a number.")
                continue

            number = int(raw)
            if not (1 <= number <= len(departments)):
                print("Invalid department number. Please try again.")
                continue

            return departments[number - 1]['department_name']
