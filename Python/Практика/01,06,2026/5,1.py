""" 05 Подсчёт посещений страниц

Реализуйте функцию, которая
- принимает список посещённых страниц
- и подсчитывает количество посещений каждой страницы, используя defaultdict.

Данные:
pages = ["home", "about", "home", "products", "home", "contact", "products"]
Пример вывода:
Посещения страниц:
{'home': 3, 'about': 1, 'products': 2, 'contact': 1}
"""

from collections import defaultdict

def count_page_visits(pages):
    result = defaultdict(int)
    for page in pages:
        result[page] += 1
    return dict(result)



pages = ["home", "about", "home", "products", "home", "contact", "products"]
sample = {'home': 3, 'about': 1, 'products': 2, 'contact': 1}

result = count_page_visits(pages)
print(result)
print(result == sample)

# {'home': 3, 'about': 1, 'products': 2, 'contact': 1}
# True
