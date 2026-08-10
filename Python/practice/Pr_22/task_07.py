""" 7. Самые популярные поисковые запросы
Добавьте в меню возможность вывести самые частые поисковые запросы, которые пользователи вводили при поиске книг.
Используйте данные из MongoDB, коллекция searches;
Сгруппируйте запросы по полю query;
Выведите запросы в порядке убывания количества;
Покажите только топ-10 самых популярных запросов;
Выводите также количество повторений для каждого.
Пример вывода:
Most frequent search queries:
1. war — 14 times
2. 1984 — 11 times
3. new — 9 times
...

"""
 # (метод для анализа):

from collections import Counter

def show_popular_queries(searches_collection):
    queries = [doc["query"].strip().lower() for doc in searches_collection.find() if doc.get("query")]
    counter = Counter(queries)
    top = counter.most_common(10)

    if not top:
        print("No search data found.")
        return

    print("Most frequent search queries:")
    for i, (query, count) in enumerate(top, start=1):
        print(f"{i}. {query} — {count} times")



