""" 02 2. Проверка на панограмму

Напишите программу, которая проверяет, содержит ли строка все буквы
английского алфавита хотя бы по одному разу (игнорируя регистр и пробелы).

Пример вывода:
Исходная строка: The quick brown fox jumps over the lazy dog
Панограмма? True
"""

text = "The quick brown fox jumps over the lazy dog".lower()

letters = ""

for ch in text:
    if ch.isalpha() and ch not in letters:
        letters += ch

is_contained = len(letters) == 26


print("Исходная строка:", text)
print("Панограмма?", is_contained)
