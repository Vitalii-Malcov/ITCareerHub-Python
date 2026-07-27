""" 02 Проверка размеров фигур

Доработайте фигуры:
Добавьте проверку в инстанцирование Circle и Rectangle,
чтобы значения были строго положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
"""

import math
from abc import ABC, abstractmethod


class InvalidSizeError(Exception):
    """Пользовательское исключение: размер фигуры не положителен."""

    def __init__(self, param_name, value):
        self.param_name = param_name
        self.value = value
        super().__init__(
            f"Значение {param_name}={value} должно быть положительным!"
        )


# ============================================================
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("radius", radius)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0:
            raise InvalidSizeError("width", width)
        if height <= 0:
            raise InvalidSizeError("height", height)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



# ============================================================
class ShapeV2(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @staticmethod
    def _validate_positive(name, value):
        # общий помощник для проверки положительности,
        # доступен всем наследникам через self._validate_positive(...)
        if value <= 0:
            raise InvalidSizeError(name, value)


class CircleV2(ShapeV2):
    def __init__(self, radius):
        self.radius = radius  # вызовет setter ниже

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._validate_positive("radius", value)
        self._radius = value

    def get_area(self):
        return math.pi * self._radius ** 2


class RectangleV2(ShapeV2):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._validate_positive("width", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._validate_positive("height", value)
        self._height = value

    def get_area(self):
        return self._width * self._height



# ============================================================
class ValidatedMixin:
    """Миксин с методом проверки положительных чисел."""

    def _check_positive(self, **kwargs):
        # kwargs: {"radius": -5} или {"width": 3, "height": 0}
        for name, value in kwargs.items():
            if value <= 0:
                raise InvalidSizeError(name, value)


class ShapeV3(ABC):
    @abstractmethod
    def get_area(self):
        pass


class CircleV3(ValidatedMixin, ShapeV3):
    def __init__(self, radius):
        self._check_positive(radius=radius)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class RectangleV3(ValidatedMixin, ShapeV3):
    def __init__(self, width, height):
        self._check_positive(width=width, height=height)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



# ============================================================
class PositiveNumber:
    """Дескриптор: хранит положительное число, иначе InvalidSizeError."""

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise InvalidSizeError(self.name, value)
        setattr(instance, self.private_name, value)


class ShapeV4(ABC):
    @abstractmethod
    def get_area(self):
        pass


class CircleV4(ShapeV4):
    radius = PositiveNumber()  # валидация "встроена" прямо в атрибут класса

    def __init__(self, radius):
        self.radius = radius  # сработает PositiveNumber.__set__

    def get_area(self):
        return math.pi * self.radius ** 2


class RectangleV4(ShapeV4):
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height



# ============================================================
from dataclasses import dataclass


class ShapeV5(ABC):
    @abstractmethod
    def get_area(self):
        pass


@dataclass
class CircleV5(ShapeV5):
    radius: float

    def __post_init__(self):
        # __post_init__ вызывается dataclass'ом сразу после __init__
        if self.radius <= 0:
            raise InvalidSizeError("radius", self.radius)

    def get_area(self):
        return math.pi * self.radius ** 2


@dataclass
class RectangleV5(ShapeV5):
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0:
            raise InvalidSizeError("width", self.width)
        if self.height <= 0:
            raise InvalidSizeError("height", self.height)

    def get_area(self):
        return self.width * self.height


if __name__ == "__main__":
    for label, Circle_, Rectangle_ in (
        ("Вариант 1 (проверка в __init__)", Circle, Rectangle),
        ("Вариант 2 (property-сеттеры)", CircleV2, RectangleV2),
        ("Вариант 3 (миксин)", CircleV3, RectangleV3),
        ("Вариант 4 (дескриптор PositiveNumber)", CircleV4, RectangleV4),
        ("Вариант 5 (dataclass + __post_init__)", CircleV5, RectangleV5),
    ):
        print(f"=== {label} ===")
        try:
            c = Circle_(-5)
        except InvalidSizeError as e:
            print("Ошибка:", e)

        try:
            r = Rectangle_(3, 0)
        except InvalidSizeError as e:
            print("Ошибка:", e)
        print()

    # Ожидаемый вывод (из условия):
    # Ошибка: Значение radius=-5 должно быть положительным!
    # Ошибка: Значение height=0 должно быть положительным!
