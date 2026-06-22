data = "яблоки 120 5, бананы 80 8, груши 150 3, апельсины 200 6, киви 90 4, манго 300 2, сливы 110 7"

goods = data.split(", ")

header = """+--------------+--------+--------+----------+
| Наименование |  Цена  | Кол-во |   Сумма  |
+--------------+--------+--------+----------+
"""

print(header, end="")

total = 0

for good in goods:
    name, price, count = good.split()
    price = float(price)
    count = int(count)

    total_price = price * count
    total += total_price

    print(f"| {name.capitalize():<12} | {price:6.2f} | {count:^6} | {total_price:8.2f} |")

print("+--------------+--------+--------+----------+")
print(f"|             ИТОГО:             | {total:8.2f} |")
print("+--------------------------------+----------+")
