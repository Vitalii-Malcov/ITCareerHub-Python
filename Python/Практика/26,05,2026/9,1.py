""" 09 Одинаковые предметы

Есть список студентов и наборы предметов, которые они изучают.
Необходимо сгруппировать студентов по идентичным наборам предметов, используя frozenset как ключ, и вывести группы.
Данные:
students = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Math", "Physics"],
    "Charlie": ["Chemistry", "Biology"],
    "David": ["Math", "Physics"],
    "Eve": ["Chemistry", "Biology"]
}

Пример вывода:
Группа с предметами: Physics, Math: ['Alice', 'Bob', 'David']
Группа с предметами: Biology, Chemistry: ['Charlie', 'Eve']
"""

students = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Math", "Physics"],
    "Charlie": ["Chemistry", "Biology"],
    "David": ["Math", "Physics"],
    "Eve": ["Chemistry", "Biology"]
}

groups = {}

for student, subjects in students.items():
    key = frozenset(subjects)
    if key not in groups:
        groups[key] = []
    groups[key].append(student)

for subjects, students_list in groups.items():
    subjects_str = ', '.join(subjects)
    students_str = ', '.join(students_list)
    print(f"Группа с предметами: {subjects_str}: [{students_str}]")
