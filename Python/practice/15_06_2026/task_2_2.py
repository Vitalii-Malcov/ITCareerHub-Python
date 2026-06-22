""" 02 Реверс строки

Напишите рекурсивную функцию, которая
- переворачивает строку.

Если передан не строковый тип, выбросить исключение.
При вызове функции обработайте возможное исключение.

Данные:
text = "recursion"
Пример вывода:
noisrucer
"""

def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError(f'Ожидается строка, получен {type(s)}')
    if len(s) == 0:
        return ''
    return s[-1] + reverse_string(s[:-1])

try:
    text = "recursion"
    result = reverse_string(text)
    print(result)
except TypeError as e:
    print(f"Ошибка: {e}")


# Шаг 9  вернул:  "r" + ""          = "r"
# Шаг 8  вернул:  "e" + "r"         = "er"
# Шаг 7  вернул:  "c" + "er"        = "cer"
# Шаг 6  вернул:  "u" + "cer"       = "ucer"
# Шаг 5  вернул:  "r" + "ucer"      = "rucer"
# Шаг 4  вернул:  "s" + "rucer"     = "srucer"
# Шаг 3  вернул:  "i" + "srucer"    = "isrucer"
# Шаг 2  вернул:  "o" + "isrucer"   = "oisrucer"
# Шаг 1  вернул:  "n" + "oisrucer"  = "noisrucer"
