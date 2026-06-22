MIN_HOURS = 0
MAX_HOURS = 23
MIN_MINUTES = 0
MAX_MINUTES = 59

hours = int(input("Введите часы: "))
minutes = int(input("Введите минуты: "))

if MIN_HOURS <= hours <= MAX_HOURS and MIN_MINUTES <= minutes <= MAX_MINUTES:
    print("Корректное время.")
else:
    print("Некорректное время.")
