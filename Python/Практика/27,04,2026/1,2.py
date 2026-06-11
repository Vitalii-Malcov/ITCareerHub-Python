""" 02 Квадрат чисел

Напишите программу, которая
- обрабатывает строку
- и заменяет все вхождения чисел в строке на их квадрат, оставляя другие части строки неизменными.

Данные:
text = "I have 2 apples and 4 bananas"
Пример вывода:
I have 4 apples and 16 bananas
"""

text = "I have 2 apples and 4 bananas"


print(text)
result = [str(int(word) ** 2) if word.isdigit() else word for word in words]
