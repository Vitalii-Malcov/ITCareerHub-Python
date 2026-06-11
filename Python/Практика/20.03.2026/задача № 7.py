
tasks = int(input("Введите количество задач: "))
time_per_task = int(input("Введите время на задачу (мин): "))

total_minutes = tasks * time_per_task

hours = total_minutes // 60
minutes = total_minutes % 60

print("Общее время: {hours} часа и {minutes} минут")
