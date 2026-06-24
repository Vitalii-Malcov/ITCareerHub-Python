import pandas as pd
import sqlite3

# Создаём словарь с данными
data = {
'column1': ['value1', 'value2', 'value3'],
'column2': ['value1', 'value2', 'value3'],
'column3': ['value1', 'value2', 'value3'],
}

# Преобразуем словарь в DataFrame
df = pd.DataFrame(data)

# Выводим таблицу
print(df)
