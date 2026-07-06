"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from collections import Counter
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rld


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_info():
    """
    "name": "Diana Williams",
    "birth_date": "12.06.1983",
    "enrollment_date": "29.04.2023",
    "courses": [
      "Physics",
      "Chemistry"
    ]
    """
    students = read_json("student_courses.json")

    total_students = len(students)

    ages_at_enrollment = []
    course_counter = Counter()

    for student in students:
        birth_date = dt.strptime(student["birth_date"], "%d.%m.%Y")
        enrollment_date = dt.strptime(student["enrollment_date"], "%d.%m.%Y")

        age = rld(enrollment_date, birth_date).years
        ages_at_enrollment.append(age)

        course_counter.update(student["courses"])

    average_age = sum(ages_at_enrollment) / total_students

    report = {
        "total_students": total_students,
        "average_age_at_enrollment": round(average_age, 2),
        "students_per_course": dict(course_counter),
    }

    write_json("student_courses_report.json", report)

    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=4, ensure_ascii=False))

get_info()
