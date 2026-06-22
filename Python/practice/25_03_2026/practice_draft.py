total = 0
n = int(input("Введите число: "))

while n != 0:
    if n > 0:
        total += n
    n = int(input("Введите число: "))

print(f"Общая сумма положительных: {total}")
