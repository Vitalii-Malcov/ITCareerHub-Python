""" 08 — Полная проверка работы"""

from task_07 import Student

""" 07. Фильтрация студентов по возрасту """


# Создание студентов
s1 = Student("Alice", "2005-05-10")
s2 = Student.from_string("Bob, 2001-12-03")

print(s1)
s1.show_info()

print(s2)
s2.show_info()

# Проверка исключения
try:
    Student("Bill", "2019-05-15")
except ValueError as e:
    print("Ошибка:", e)

# Фильтрация
res = Student.filter_by_min_age([s1, s2], 21)
print("Min age 21:")
for s in res:
    print("\t", s)


# [Student: Alice, birth_date: 2005-05-10, ID: 1,
#  Student: Bob, birth_date: 2001-12-03, ID: 2]
# Student: Alice, birth_date: 2005-05-10, ID: 4
# Student:
#     Name: Alice
#     Age: 20
#     ID: 4
# Student: Bob, birth_date: 2001-12-03, ID: 5
# Student:
#     Name: Bob
#     Age: 24
#     ID: 5
# Ошибка: Student must be at least 16 years old.
# Min age 20:
# 	 Student: Alice, birth_date: 2005-05-10, ID: 4
# 	 Student: Bob, birth_date: 2001-12-03, ID: 5
#
# Process finished with exit code 0
