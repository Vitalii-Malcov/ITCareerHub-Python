from timeit import timeit


def merge_dicts_1(*dicts):
    """Объединяет любое количество словарей в один. При совпадении ключей побеждает последний."""
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = value
    return result

def merge_dicts_2(*dicts):
    """Объединяет любое количество словарей в один. При совпадении ключей побеждает последний."""
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

def merge_dicts_3(*dicts):
    result = {}
    for d in dicts:
        result = result | d
    return result


def merge_dicts_4(*dicts):
    result = {}
    for d in dicts:
        result = {**result, **d}
    return result


def merge_dicts_5(*dicts):
    return {k: v for d in dicts for k, v in d.items()}


def merge_dicts_6(*dicts):
    result = dicts[0].copy()   # берём первый словарь
    for d in dicts[1:]:        # идём со второго
        result.update(d)
    return result


d1 = {i: i*2 for i in range(10000)}
d2 = {i: i*3 for i in range(10000, 20000)}
d3 = {i: i*4 for i in range(20000, 30000)}


print(timeit(lambda: merge_dicts_1(d1, d2, d3), number=10000))
print(timeit(lambda: merge_dicts_2(d1, d2, d3), number=10000))
print(timeit(lambda: merge_dicts_3(d1, d2, d3), number=10000))
print(timeit(lambda: merge_dicts_4(d1, d2, d3), number=10000))
print(timeit(lambda: merge_dicts_5(d1, d2, d3), number=10000))
print(timeit(lambda: merge_dicts_6(d1, d2, d3), number=10000))


# print(timeit(merge_dicts_1, number=1_000_000))
# print(timeit(merge_dicts_2, number=1_000_000))

# from timeit import timeit
#
# # Создаём большие словари для теста

#
# print(timeit(lambda: merge_dicts_1(d1, d2, d3), number=10000))
# print(timeit(lambda: merge_dicts_2(d1, d2, d3), number=10000))
