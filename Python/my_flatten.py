def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(tuple(flatten(nested_numbers)))  # 7

# Пример использования:
# nested = [1, [2, 3], [4, [5, 6]], 7]
# flat = list(flatten(nested))   -> [1, 2, 3, 4, 5, 6, 7]
# total = sum(flatten(nested))   -> 28
