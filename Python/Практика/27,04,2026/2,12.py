""" 12 По одному пробелу

Напишите программу, которая
- удаляет в строке лишние пробелы, оставляя только по одному пробелу между словами.

text = " Hello, World! How are you? "
Пример вывода:
Строка: '    Hello,     World!  How  are   you?    '
Результат: 'Hello, World! How are you?'
"""

text = " Hello, World! How are you? "

print(' '.join(text.split()))
