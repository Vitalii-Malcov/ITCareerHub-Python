
km = int(input("Введите расстояние (в км): "))
fuel_per_100 = float(input("Введите расход: "))
price = float(input("Введите цену: "))

fuel = (km / 100) * fuel_per_100
total = fuel * price

print("Стоимость бензина:", total)
