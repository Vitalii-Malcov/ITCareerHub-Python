import json
from datetime import datetime
from collections import defaultdict


MONTH_TO_QUARTER = {
    1: "Q1", 2: "Q1", 3: "Q1",
    4: "Q2", 5: "Q2",
    9: "Q3", 10: "Q3", 11: "Q3", 12: "Q3",
}


def get_quarter(date_str) -> str | None:
    date = datetime.strptime(date_str, "%d-%m-%Y")
    return MONTH_TO_QUARTER.get(date.month)


def read_grades(file_path="grades.json") -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def group_recursive(items, key_funcs, agg_func):
    if not key_funcs:
        return agg_func(items)

    key_func, *rest_key_funcs = key_funcs

    groups = defaultdict(list)
    for item in items:
        groups[key_func(item)].append(item)

    return {
        key: group_recursive(sub_items, rest_key_funcs, agg_func)
        for key, sub_items in sorted(groups.items())
    }


def calculate_quarterly_averages(data) -> dict:
    filtered = [entry for entry in data if get_quarter(entry["date"]) is not None]

    key_funcs = [
        lambda entry: entry["name"],
        lambda entry: entry["subject"],
        lambda entry: get_quarter(entry["date"]),
    ]

    def average(entries):
        grades = [entry["grade"] for entry in entries]
        return round(sum(grades) / len(grades), 2)

    return group_recursive(filtered, key_funcs, average)


def save_report(report, file_path="grades_quarterly_report.json") -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)


def generate_quarterly_report(input_file="grades.json", output_file="grades_quarterly_report_2.json") -> None:
    data = read_grades(input_file)
    report = calculate_quarterly_averages(data)
    save_report(report, output_file)
    print(f"Отчет успешно сохранен в {output_file}")


generate_quarterly_report()
