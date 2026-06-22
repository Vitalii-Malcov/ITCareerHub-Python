"""05 Распаковка матрицы
Дан двумерный список (матрица).
Создайте новый список, содержащий все элементы матрицы в одном измерении (список).
Данные:
matrix = [[1, 2], [3, 4], [5, 6]]

Пример вывода:
[1, 2, 3, 4, 5, 6]
"""

matrix = [[1, 2], [3, 4], [5, 6]]

flattened = [item for sublist in matrix for item in sublist]

print(flattened)

# 2 Вариант
matrix = [[1, 2], [3, 4], [5, 6]]


result = []

for row in matrix:
    for num in row:
        result.append(num)

print(result)
