# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
#
# text = "My number is 123-456-789"
#
# Пример вывода:
#
# Строка: My number is 123-456-789
#
# Результат: My number is ***-***-***

text = "My number is 123-456-789"

print("Строка:", text)

result = ""

for ch in text:
    if ch.isdigit():
        result += "*"
    else:
        result += ch

#result = "".join("*" if ch.isdigit() else ch for ch in text)

print("Результат:", result)






