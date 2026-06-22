""" 13 Очередь заказов

Реализуйте очередь для обработки заказов, пока пользователь не введет "exit".
Далее отобразите
- самый ранний заказ,
- а также оставшиеся заказы
- и их количество.

Пример вывода:
Введите заказ или "exit" для завершения: Pizza
Введите заказ или "exit" для завершения: Burger
Введите заказ или "exit" для завершения: Pasta
Введите заказ или "exit" для завершения: exit
Первый заказ: Pizza
Осталось 2 заказов:
	- Burger
	- Pasta
"""

from collections import deque

queue = deque()

while True:
    order = input("Введите заказ или \"exit\" для завершения: ")

    if order == "exit":
        break

    queue.append(order)

if not queue:
    print("Пустая очередь")
    exit()

print("Первый заказ:", queue.popleft())

print("Осталось", len(queue), "заказов:")

for order in queue:
    print("-", order)

# 2 Вариант
#
# from collections import deque
#
# queue = deque(["Pizza", "Burger", "Pasta"])
#
# while True:
#     order = input("Введите заказ или \"exit\" для завершения: ")
#     if order == "exit":
#         break
#     queue.append(order)
#
# first = queue.popleft()
#
# print("Первый заказ: ", first)
# print("Осталось:", len(queue), "Заказов:")
#
# for item in queue:
#     print("\t-", item)
