"""02 Группировка студентов по классам

Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.

Данные:
students = [
    ("class1", "Alice"),
    ("class2", "Bob"),
    ("class1", "Charlie"),
    ("class3", "Daisy")
]

Пример вывода:
{
    'class1': ['Alice', 'Charlie'],
    'class2': ['Bob'],
    'class3': ['Daisy']
}
"""

from collections import defaultdict

def get_students_groups(students):
    groups = defaultdict(list)
    for class_name, student_name in students:
        groups[class_name].append(student_name)
    return dict(groups)


def get_students_groups_2(students):
    groups = {}
    for key, value in students:
        groups[key] = groups.get(key, []) + [value]
    return groups

def get_students_groups_3(students):
    keys = {key for key, value in students}
    return {key: [v for k, v in students if k == key] for key in keys}

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
sample = {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}


functions = [get_students_groups, get_students_groups_2, get_students_groups_3]
for func in functions:
    result = func(students)
    print(
        *[f"{key}: {value}" for key, value in result.items()],
        result == sample,
        "",
        sep="\n"
    )
