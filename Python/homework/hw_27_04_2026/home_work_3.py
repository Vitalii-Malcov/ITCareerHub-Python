# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
#
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# Пример вывода:
#
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

result = ""  # итоговая строка
num = ""     # накапливаем цифры и точки

for ch in text:
    if ch.isdigit() or ch == ".":
        num += ch  # добавляем символ к числу
    else:
        if num:  # если накопили что-то числовое
            if num.count(".") <= 1 and num[0] != "." and num[-1] != ".":# валидное число: не более одной точки и точка не на краях
                result += str(float(num) * 10)  # умножаем на 10
            else:
                result += num  # не число — добавляем как есть (....3672.)
            num = ""  # сбрасываем накопленное
        result += ch  # добавляем текущий не-числовой символ
print(result)
