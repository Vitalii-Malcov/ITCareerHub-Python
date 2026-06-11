

num = int(input("Введите четырёхзначное число: "))

first = num // 1000        # первая цифра
last = num % 10            # последняя цифра

middle = (num // 10) % 100 # середина

new_num = last * 1000 + middle * 10 + first

print("Новое число:", new_num)
