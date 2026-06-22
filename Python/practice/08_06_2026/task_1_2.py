""" 1.2. Фильтрация чётных с filter

Выполните те же условия, что в задаче "Фильтрация списка с функцией", но решите с помощью filter и lambda.
"""

nums = [1, 2, 3, 4, 5, 6]
sample = [2, 4, 6]

result = list(filter(lambda num: num % 2 == 0, nums))
print(result)            # [2, 4, 6]
print(result == sample)  # True
