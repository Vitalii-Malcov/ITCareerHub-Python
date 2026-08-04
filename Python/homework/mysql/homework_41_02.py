""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода 1:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560

Пример вывода 2:
Введите страну: Unknown
❌ Страна 'Unknown' не найдена
...

"""

import mysql.connector

from homework_41_01 import DatabaseError, WorldDB as WorldDB01, dbconfig


class WorldDB(WorldDB01):
    """
    Расширяем WorldDB из задачи 01 новым методом.
    fetch_countries() и подключение (через MySQLConnection) наследуются
    как есть, дублировать их код здесь не нужно.
    """

    def fetch_cities_by_country(self, country_name):
        """
        Получить все города выбранной страны с их населением
        (отсортированы по убыванию численности населения).

        Поиск страны нечувствителен к регистру (LOWER),
        так что "germany", "Germany", "GERMANY" — сработают одинаково.
        Если страна не найдена — поднимаем DatabaseError,
        чтобы main поймал её и вывел единое сообщение "...".
        """
        try:
            self.cursor.execute(
                "SELECT Code, Name FROM country WHERE LOWER(Name) = LOWER(%s)",
                (country_name,)
            )
            country = self.cursor.fetchone()
            if country is None:
                raise DatabaseError(f"Страна '{country_name}' не найдена")

            self.cursor.execute(
                """
                SELECT Name, District, Population
                FROM city
                WHERE CountryCode = %s
                ORDER BY Population DESC
                """,
                (country["Code"],),
            )
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка при получении списка городов: {e}")


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            countries = db.fetch_countries()
            print("Список стран:")
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")

            country_input = input("\nВведите страну: ").strip()

            cities = db.fetch_cities_by_country(country_input)

            if not cities:
                print(f"Для страны '{country_input}' нет данных о городах.")
            else:
                for city in cities:
                    city_name = city["Name"]
                    population = city["Population"]
                    print(f"{city_name} — {population}")

    except DatabaseError as e:
        print(f"❌ {e}")
