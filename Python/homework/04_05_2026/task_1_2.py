""" 02 Повторяющиеся элементы

Напишите программу, которая
- находит индексы элементов тюпла, встречающихся более одного раза.
- Вывести сами элементы и их индексы.

Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 	1 4 9
Индексы элемента 3: 	2 6
Индексы элемента 4: 	3 8
"""

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

# use = ()
#
# for i, num in enumerate(numbers):
#     if num not in use:
#         indides = ()
#
#         for j, value in enumerate(numbers):
#             if value == num:
#                 indides += (j,)
#
#         if len(indides) > 1:
#             print('Инденкс элемента', num, ":\t", *indides)
#
#         use += (num,)

use = ()
for i in range(len(numbers)):
    num = numbers[i]
    if num not in use:
        count = 0

        for j in range(len(numbers)):
            if num == numbers[j]:
                count += 1
        if count > 1:
            print('Инденкс элемента', num, ":\t", end=' ')

            for j in range(len(numbers)):
                if num == numbers[j]:
                    print(j, end=' ')
            print()
        use += (num,)

