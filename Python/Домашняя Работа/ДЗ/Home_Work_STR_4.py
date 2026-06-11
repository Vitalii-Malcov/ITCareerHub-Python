text = input("Введите строку: ")

text = text[::-1]

result = ""

i = 0

while i < len(text):
    if not text[i].isdigit():
        result += text[i]
    i += 1

print("Результат:", result)
