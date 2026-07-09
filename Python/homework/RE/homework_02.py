"""2. Разделение списка тегов
Реализуйте программу, которая должна:
Прочитать строку с тегами, введёнными пользователем.
Разделить её на отдельные теги, независимо от того,
чем они были разделены (запятые, точки с запятой, слэши или пробелы).
Удалить лишние пробелы и пустые значения.

Данные:
tag_input = "python, data-science / machine-learning; AI  neural-networks"

Пример вывода:
['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']
"""


tag_input = "python, data-science / machine-learning; AI  neural-networks"

import re
from functools import reduce

tags = [t.strip() for t in re.split(r'[,;/\s]+', tag_input) if t.strip()]
tags_1 = list(filter(None, (t.strip() for t in re.split(r'[,;/\s]+', tag_input))))
tags_2 = re.findall(r'[\w-]+', tag_input)
tags_3 = reduce(lambda s, ch: s.replace(ch, ' '), ',;/', tag_input).split()

print(tags, '\n', tags_1, '\n', tags_2, '\n', tags_3)

# ['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']
