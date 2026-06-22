""" 04 Сумма продаж

Есть дерево подразделений внутри компании
(каждое подразделение может содержать «дочерние» отделы).
Напишите рекурсивную функцию, которая
- подсчитывает суммарные продажи для всех отделов.

Функция должна проверять:
- Аргумент должен быть словарем.
- Дочерние отделы (если есть) должны быть списком словарей.

Если данные не валидны необходимо выбрасывать исключение.
При вызове функции обработайте возможное исключение.

Данные:
company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

Пример вывода:
Общая сумма продаж: 1140
"""

company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}


def summarize_sales(department: dict) -> int:
    if not isinstance(department, dict):
        raise TypeError(f"Подразделение должно быть словарём, получено: {type(department)}")
    total: int = department.get("sales", 0)
    if "sub_departments" in department:
        sub_departments = department["sub_departments"]
        if not isinstance(sub_departments, list):
            raise TypeError(f"sub_departments должен быть списком, получено: {type(sub_departments)}")
        for sub in sub_departments:
            if not isinstance(sub, dict):
                raise TypeError(f"Каждый дочерний отдел должен быть словарём, получено: {type(sub)}")
            total += summarize_sales(sub)
    return total

try:
    result = summarize_sales(company_structure)
    print(f"Общая сумма продаж: {result}")
except TypeError as e:
    print(f"Ошибка валидации данных: {e}")


# Head Office (100)
# Sales Department (200)
# B2B Sales (120)
# IT Department (150)
# DevOps (300)
# Cloud Infrastructure (180)
# QA Department (90)
#
# 100 + 200 + 120 + 150 + 300 + 180 + 90 = 1140
