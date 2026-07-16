""" 01 Класс Rectangle

Создайте класс Rectangle, который описывает прямоугольник.
У каждого объекта должны быть два поля:
- width
- и height.
Добавьте метод get_area(), который возвращает площадь прямоугольника.
Создайте объект прямоугольника с произвольными значениями.
Выведите его площадь.
Измените ширину и высоту.
Выведите новую площадь.

Пример вывода:
Площадь: 20
Новая площадь: 35

"""

from dataclasses import dataclass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



@dataclass
class RectangleDataclass:
    width: float
    height: float

    def get_area(self):
        return self.width * self.height


class RectangleSlots:
    __slots__ = ("width", "height")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


if __name__ == "__main__":
    print("--- Вариант 1: классический ---")
    rect = Rectangle(4, 5)
    print("Площадь:", rect.get_area())
    rect.width = 7
    rect.height = 5
    print("Новая площадь:", rect.get_area())

    print("\n--- Вариант 2: dataclass ---")
    rect2 = RectangleDataclass(4, 5)
    print("Площадь:", rect2.get_area())
    rect2.width = 7
    rect2.height = 5
    print("Новая площадь:", rect2.get_area())

    print("\n--- Вариант 3: __slots__ ---")
    rect3 = RectangleSlots(4, 5)
    print("Площадь:", rect3.get_area())
    rect3.width = 7
    rect3.height = 5
    print("Новая площадь:", rect3.get_area())

