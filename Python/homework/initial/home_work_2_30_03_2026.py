

year = int(input("Введите год: "))

if year % 400 == 0:
    print("Високосный год")
elif year % 100 == 0:
    print("Не високосный год")
elif year % 4 == 0:
    print("Високосный год")
else:
    print("Не високосный год")

# второй вариант

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Високосный год")
else:
    print("Не високосный год")
