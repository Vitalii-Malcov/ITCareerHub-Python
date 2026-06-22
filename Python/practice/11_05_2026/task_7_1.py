""" 07 Упаковка товаров по ящикам

У вас есть список весов товаров.
Каждый ящик может выдержать не более заданного веса.
Напишите программу, которая
- распределяет товары по минимальному количеству ящиков, не превышая допустимый вес.

Данные:
weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]

Пример вывода:
Введите максимальный вес ящика: 10
Распределение по ящикам:
Ящик 1: [9, 1]
Ящик 2: [8, 2]
Ящик 3: [7, 3]
Ящик 4: [6, 4]
Ящик 5: [5, 4, 1]
Ящик 6: [3, 2, 1]
"""
weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]
max_weight = 10

sorted_weights = sorted(weights, reverse=True)
boxes = []

for w in sorted_weights:
    placed = False
    for box in boxes:
        if sum(box) + w <= max_weight:
            box.append(w)
            placed = True
            break
    if not placed:
        boxes.append([w])

print("Распределение по ящикам:")
for i, box in enumerate(boxes, 1):
    print(f"Ящик {i}: {box}")
