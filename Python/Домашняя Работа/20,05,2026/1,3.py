
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
d={}
for number in numbers:
    d[number] = d.get(number, 0) + 1
print(d)
# print(d.items())

# почему-то дает ошибку в 23 строке...
for k in d:
    if d[k] == 1:
        _ = d.pop(k)
        del d[k]
print(d)
print(sorted(d.keys(), reverse=True))

key_list = [k for k, v in d.items() if v > 1]
print(sorted(key_list, reverse=True))
