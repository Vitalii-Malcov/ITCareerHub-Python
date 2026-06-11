names = ['John', 'Bob', 'Alice', 'Anna', 'Mark']  # Список имён

total_length = 0  # Переменная для суммы длин всех имён

for name in names:  # Цикл по каждому имени в списке
    total_length += len(name)  # Добавляем длину текущего имени к сумме

average = total_length / len(names)  # Вычисляем среднюю длину имён

print("Средняя длина имён:", average)  # Выводим среднюю длину

result = [name for name in names if len(name) > average]  # Создаём список имён, которые длиннее средней

print("Имена длиннее средней длины:", result)  # Выводим результат
