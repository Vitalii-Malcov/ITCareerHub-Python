"""Не уникальные числа
Напишите программу, которая находит все числа, встречающиеся
более одного раза в списке, и выводит их в порядке убывания.
Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
Пример вывода:
Числа, встречающиеся более одного раза: [7, 4, 3, 8]"""

# numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
#
# d = {}# считаем количество повторений
#
# for num in numbers:
#     if num not in d:
#         d[num] = 1
#     else:
#         d[num] += 1
#
# result = []# собираем только повторяющиеся числа
#
# for num in d:
#     if d[num] > 1:
#         result.append(num)
#
# for i in range(len(result)):# ручная сборка
#     for j in range(i + 1, len(result)):
#         if d[result[i]] < d[result[j]]:# если повторений справа больше
#             result[i], result[j] = result[j], result[i]#Сначала сравниваем количество повторений
#         elif d[result[i]] == d[result[j]]:# если количество повторений одинаковое
#             if result[i] < result[j]:#сортируем по убыванию
#                 result[i], result[j] = result[j], result[i]
#
# print("Числа, встречающиеся более одного раза:", result)


numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

d = {}

for num in numbers:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

dict2 = {}

for num in d:
    count = d[num]
    if count not in dict2:
        dict2[count] = []
    dict2[count].append(num)
for count in dict2:
    dict2[count].sort(reverse=True)

result = []
sorted_counts = sorted(dict2.keys(), reverse=True)

for count in sorted_counts:
    if count > 1:
        result += dict2[count]
print("Числа, встречающиеся более одного раза:", result)


numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
d = {}
for num in numbers:
    d[num] = d.get(num,0) + 1
dict2 = {}
for num, count in d.items():
    if count not in dict2:
        dict2[count] = []
    dict2[count].append(num)

for nums in dict2.values():
    nums.sort(reverse=True)

result = []
for count in sorted(dict2, reverse=True):
    if count > 1:
        result.extend(dict2[count])

print(result)
