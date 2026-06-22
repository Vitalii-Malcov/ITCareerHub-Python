text = input("Введите числа через пробел: ")

numbers = []
num = ''


for char in text:
    if char == ' ':
        numbers = numbers + [int(num)]
        num = ''
    else:
        num = num + char

numbers = numbers + [int(num)]

half = len(numbers) // 2

result = numbers[:half] + numbers[:half][::-1]

print('Результат:', result)
