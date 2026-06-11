numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

result = []
idxs = []
k = 0
for i, num in enumerate(numbers):
    if num not in result and numbers.count(num) > 1:
        result += [num,[]]
        for j, value in enumerate(numbers):
            if value == num:
                idxs += [j]

        result[k * 2 + 1] = idxs
        idxs = []
        k += 1
for i in range(0, len(result), 2):
    print('Индексы элемента', result[i], ":\t", *result[i + 1])
