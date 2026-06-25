""" 01 План по дням недели

Напишите программу, которая помогает планировать дела.
Программа должна
- бесконечно выводить план на следующий день недели,
- пока пользователь нажимает 'Enter'.

Данные:
# Расписание дел на неделю
weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"]
}

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q
"""


from itertools import cycle

weekly_schedule = {
    "Monday": ["Gym", "Work", "Read book"],
    "Tuesday": ["Meeting", "Work", "Study Python"],
    "Wednesday": ["Shopping", "Work", "Watch movie"],
    "Thursday": ["Work", "Call parents", "Play guitar"],
    "Friday": ["Work", "Dinner with friends"],
    "Saturday": ["Hiking", "Rest"],
    "Sunday": ["Family time", "Rest"],
}

for day, tasks in cycle(weekly_schedule.items()):
    if input("Нажмите 'Enter' для получения плана: "):  # любой ввод, кроме Enter → выход
        break
    print(f"{day}: {', '.join(tasks)}")


######################################################################################

def get_product(clothes, colors, sizes):
    for clothe in clothes:
        for color in colors:
            for size in sizes:
                print(f"{clothe} - {color} - {size}")


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

get_product(clothes, colors, sizes)


