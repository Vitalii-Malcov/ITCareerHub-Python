""" 02 Класс Counter

Реализуйте класс Counter, который представляет собой простой счётчик.
Счётчик должен начинаться с нуля.
Предусмотрите методы
- для увеличения
- и уменьшения значения на единицу,
при этом при каждой операции должно отображаться новое значение счётчика.

Добавьте метод, возвращающий текущий результат.
Проверьте работу счётчика, выполнив несколько операций.

Пример вывода:
Значение увеличено, текущее: 1
Значение увеличено, текущее: 2
Значение увеличено, текущее: 3
Значение уменьшено, текущее: 2
Текущее значение: 2
"""



class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1
        print("Значение увеличено, текущее:", self.value)

    def decrease(self):
        self.value -= 1
        print("Значение уменьшено, текущее:", self.value)

    def get_value(self):
        print("Текущее значение:", self.value)


class CounterStep:
    def __init__(self):
        self.value = 0

    def increase(self, step=1):
        self.value += step
        print("Значение увеличено, текущее:", self.value)

    def decrease(self, step=1):
        self.value -= step
        print("Значение уменьшено, текущее:", self.value)

    def get_value(self):
        print("Текущее значение:", self.value)

class CounterBounded:
    def __init__(self, min_value=None, max_value=None):
        self.value = 0
        self.min_value = min_value
        self.max_value = max_value

    def increase(self):
        if self.max_value is not None and self.value >= self.max_value:
            print(f"Достигнут максимум ({self.max_value}), увеличение невозможно")
            return
        self.value += 1
        print("Значение увеличено, текущее:", self.value)

    def decrease(self):
        if self.min_value is not None and self.value <= self.min_value:
            print(f"Достигнут минимум ({self.min_value}), уменьшение невозможно")
            return
        self.value -= 1
        print("Значение уменьшено, текущее:", self.value)

    def get_value(self):
        print("Текущее значение:", self.value)


class CounterWithRepr:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += 1
        print("Значение увеличено, текущее:", self.value)

    def decrease(self):
        self.value -= 1
        print("Значение уменьшено, текущее:", self.value)

    def get_value(self):
        print("Текущее значение:", self.value)

    def __str__(self):
        return f"Counter(value={self.value})"

if __name__ == "__main__":
    print("--- Вариант 1: классический ---")
    counter = Counter()
    counter.increase()
    counter.increase()
    counter.increase()
    counter.decrease()
    counter.get_value()

    print("\n--- Вариант 2: с шагом (step) ---")
    counter2 = CounterStep()
    counter2.increase()  # +1 по умолчанию
    counter2.increase(step=5)  # +5
    counter2.decrease(step=2)  # -2
    counter2.get_value()

    print("\n--- Вариант 3: с ограничением (max=2) ---")
    counter3 = CounterBounded(min_value=0, max_value=2)
    counter3.increase()
    counter3.increase()
    counter3.increase()  # уже упрёмся в максимум
    counter3.decrease()
    counter3.get_value()

    print("\n--- Вариант 4: с __str__ ---")
    counter4 = CounterWithRepr()
    counter4.increase()
    counter4.increase()
    counter4.increase()
    counter4.decrease()
    counter4.get_value()
    print("print(counter4):", counter4)
