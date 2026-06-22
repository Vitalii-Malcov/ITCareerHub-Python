
import pandas as pd
import sqlite3
from tabulate import tabulate

def main():
    data = {
        "Дата": [
            "12.06.2026",
            "13.06.2026",
            "14.06.2026",
            "15.06.2026",
            "16.06.2026",
            "17.06.2026",
            "18.06.2026"
        ],
        "Температура днем, °C": [22, 24, 19, 21, 25, 20, 23],
        "Температура ночью, °C": [14, 15, 12, 13, 16, 11, 14],
        "Продолжительность светового дня": [
            "16 ч 20 мин",
            "16 ч 21 мин",
            "16 ч 22 мин",
            "16 ч 23 мин",
            "16 ч 24 мин",
            "16 ч 25 мин",
            "16 ч 26 мин"
        ],
        "Скорость ветра, км/ч": [15, 7, 5, 4, 6, 2, 8],
        "Влажность, %": [60, 65, 55, 50, 70, 45, 75],
        "Атмосферное давление, гПа": [1015, 1013, 1018, 1012, 1016, 1014, 1017]
    }

    # Создаём таблицу DataFrame
    weather_df = pd.DataFrame(data)

    print("Таблица pandas:")
    print(tabulate(weather_df, headers='keys', tablefmt='grid', showindex=False))

    # Создаём подключение к базе данных SQLite
    conn = sqlite3.connect("weather.db")

    # Записываем DataFrame в таблицу weather
    weather_df.to_sql("weather", conn, if_exists="replace", index=False)

    # Читаем данные обратно из базы данных
    weather_from_db = pd.read_sql_query("SELECT * FROM weather", conn)

    print("\nТаблица из базы данных SQLite:")
    print(tabulate(weather_from_db, headers='keys', tablefmt='grid', showindex=False))

    # Закрываем соединение с базой данных
    conn.close()


if __name__ == "__main__":
    main()
