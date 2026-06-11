#distance = float(input("Введите расстояние (в км): "))
#speed = float(input("Введите скорость (км/ч): "))

#time = distance / speed

#print("Время в пути:", time, "часов")


distance = int(input("Введите расстояние (в км): "))
speed = float(input("Введите скорость (км/ч): "))

time = distance / speed

hours = int(time)
minutes = int((time - hours) * 60)

print(f"Время в пути: {hours} часа и {minutes} минут")
