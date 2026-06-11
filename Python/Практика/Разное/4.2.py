

text = input("Введите числа через пробел: ")

numbers = []
num = ""

for char in text:
    if char == ' ':
        numbers += [int(num)]
        num = ''
    else:
        num += char

numbers += [int(num)]

length = len(numbers)

half = length // 2
first_half = numbers[:half]
reversed_half = first_half[::-1]
result = first_half + reversed_half

print('Результат:', result)
