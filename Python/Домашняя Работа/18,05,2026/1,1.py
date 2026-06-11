""" 01 Проверка на подмножество

Напишите программу, которая
- проверяет, содержит ли первое множество все элементы второго множества.

Реализуйте решение несколькими способами.
(в том числе и способом, НЕ используящим возможности множеств).

Данные:
set1 = {1, 2, 3, 4}
set2 = {2, 3}
Пример вывода:
True
"""
set1 = {1, 2, 3, 4}
set2 = {2, 3}

result = True
for n in set2:
    if n not in set1:
        result = False
        break
print(result)

print(set2 <= set1)
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set1 & set2 == set2)
