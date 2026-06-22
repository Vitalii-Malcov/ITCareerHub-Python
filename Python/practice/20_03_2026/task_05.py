

days = int(input("Введите количество дней: "))

weeks = days // 7
rest_days = days % 7

print(f"До события осталось: {weeks} недель и {rest_days} дня")
