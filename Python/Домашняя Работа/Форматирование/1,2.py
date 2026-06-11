
# Напишите программу, которая принимает список строк в формате
# "name age balance" и выводит информацию о каждом человеке с
# отформатированными данными: имя — 10 символов, возраст — 3 символа,
# баланс — 10 символов с двумя знаками после запятой. Используйте заранее подготовленный список строк.
# Данные:
# data_list = [
#     "John 23 12345.678",
#     "Alice 30 200.50",
#     "Bob 35 15000.3",
#     "Charlie 40 500.75"

data_list = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"
]

# for line in data_list:
#     parts = line.split()
#     name = parts[0]
#     age = int(parts[1])
#     balance = float(parts[2])
#     print(f"{name:<10} {age:>3} {balance:>10.2f}")



for line in data_list:
    parts = line.split()
    print("%-10s %3d %10.2f" % (parts[0], int(parts[1]), float(parts[2])))
