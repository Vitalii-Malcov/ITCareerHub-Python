"""01 Фигуры и площади

Создайте абстрактный класс Shape.
В классе должен быть метод get_area(), который возвращает площадь фигуры.
Реализуйте два класса:
- Circle, который принимает радиус.
- Rectangle, который принимает ширину и высоту.
"""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    """Абстрактный базовый класс фигуры."""

    @abstractmethod
    def get_area(self):
        """Возвращает площадь фигуры. Должен быть переопределён в наследниках."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# ============================================================
class ShapeV2(ABC):
    @property
    @abstractmethod
    def area(self):
        """Площадь доступна как свойство, а не как обычный метод."""
        pass

    def get_area(self):
        # get_area просто делегирует вызов свойству area
        return self.area


class CircleV2(ShapeV2):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


class RectangleV2(ShapeV2):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


# ============================================================
class ShapeV3(ABC):
    __slots__ = ()  # базовый класс не хранит данных сам по себе

    @abstractmethod
    def get_area(self):
        pass

    def __repr__(self):
        fields = ", ".join(
            f"{slot}={getattr(self, slot)!r}" for slot in self.__slots__
        )
        return f"{self.__class__.__name__}({fields})"


class CircleV3(ShapeV3):
    __slots__ = ("radius",)

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class RectangleV3(ShapeV3):
    __slots__ = ("width", "height")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# ============================================================
class ShapeV4(ABC):
    @abstractmethod
    def get_area(self):
        pass


@dataclass
class CircleV4(ShapeV4):
    radius: float  # dataclass сам создаст __init__(self, radius)

    def get_area(self):
        return math.pi * self.radius ** 2


@dataclass
class RectangleV4(ShapeV4):
    width: float
    height: float

    def get_area(self):
        return self.width * self.height


# ============================================================
class ShapeV5:
    def __init__(self, area_formula, **dimensions):
        # area_formula — функция, которая по размерам считает площадь
        # dimensions — именованные параметры фигуры (radius / width,height)
        self._area_formula = area_formula
        self._dimensions = dimensions
        for name, value in dimensions.items():
            setattr(self, name, value)

    def get_area(self):
        return self._area_formula(**self._dimensions)


def circle_area(radius):
    return math.pi * radius ** 2


def rectangle_area(width, height):
    return width * height


def CircleV5(radius):
    # фабричная функция, имитирующая класс Circle,
    # но фактически создающая ShapeV5 с нужной формулой
    return ShapeV5(circle_area, radius=radius)


def RectangleV5(width, height):
    return ShapeV5(rectangle_area, width=width, height=height)


if __name__ == "__main__":
    print("=== Вариант 1: classic ABC ===")
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print("Площадь круга:", circle.get_area())
    print("Площадь прямоугольника:", rectangle.get_area())

    print("\n=== Вариант 2: area через property ===")
    circle2 = CircleV2(5)
    rectangle2 = RectangleV2(4, 6)
    print("Площадь круга:", circle2.get_area())
    print("Площадь прямоугольника:", rectangle2.get_area())

    print("\n=== Вариант 3: __slots__ + __repr__ ===")
    circle3 = CircleV3(5)
    rectangle3 = RectangleV3(4, 6)
    print("Площадь круга:", circle3.get_area())
    print("Площадь прямоугольника:", rectangle3.get_area())
    print(circle3)
    print(rectangle3)

    print("\n=== Вариант 4: dataclass + ABC ===")
    circle4 = CircleV4(5)
    rectangle4 = RectangleV4(4, 6)
    print("Площадь круга:", circle4.get_area())
    print("Площадь прямоугольника:", rectangle4.get_area())
    print(circle4)
    print(rectangle4)

    print("\n=== Вариант 5: Strategy pattern (формула через функцию) ===")
    circle5 = CircleV5(5)
    rectangle5 = RectangleV5(4, 6)
    print("Площадь круга:", circle5.get_area())
    print("Площадь прямоугольника:", rectangle5.get_area())

    # Ожидаемый вывод (из условия):
    # Площадь круга: 78.53981633974483
    # Площадь прямоугольника: 24
