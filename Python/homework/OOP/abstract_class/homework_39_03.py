"""Собственный вариант: фигуры, площади и валидация — единое решение.

Объединяет оба задания (39_01 и 39_02) в одном модуле:

- дескриптор PositiveNumber — валидация переиспользуется без copy-paste;
- реестр подклассов через __init_subclass__ — фабрика Shape.create(...)
  без ручного if/elif на каждый новый тип фигуры.
"""

import math
from abc import ABC, abstractmethod
from functools import total_ordering


class InvalidSizeError(Exception):
    """Размер фигуры не положителен."""

    def __init__(self, param_name, value):
        self.param_name = param_name
        self.value = value
        super().__init__(f"Значение {param_name}={value} должно быть положительным!")


class PositiveNumber:
    """Дескриптор положительного числа. Один раз написан — используется везде."""

    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise InvalidSizeError(self.name, value)
        setattr(instance, self.private_name, value)


@total_ordering
class Shape(ABC):
    """Абстрактная фигура: умеет считать площадь и сравнивается по ней.
    Дочерние классы автоматически регистрируются в _registry по имени
    в нижнем регистре, поэтому Shape.create("circle", radius=5) работает
    для любого будущего наследника без единой правки в этом классе.
    """

    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Shape._registry[cls.__name__.lower()] = cls

    @abstractmethod
    def get_area(self):
        ...

    @classmethod
    def create(cls, kind, **dimensions):
        try:
            shape_cls = cls._registry[kind.lower()]
        except KeyError:
            known = ", ".join(cls._registry)
            raise ValueError(f"Неизвестная фигура {kind!r}. Доступны: {known}")
        return shape_cls(**dimensions)

    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return math.isclose(self.get_area(), other.get_area())

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.get_area() < other.get_area()

    def __repr__(self):
        # __slots__ хранит приватные имена (_radius), а наружу мы хотим
        # показать публичные (radius), поэтому снимаем ведущий "_"
        fields = ", ".join(
            f"{s.lstrip('_')}={getattr(self, s)!r}" for s in self.__slots__
        )
        return f"{self.__class__.__name__}({fields})"


class Circle(Shape):
    __slots__ = ("_radius",)
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius  # проходит через дескриптор -> InvalidSizeError при <= 0

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    __slots__ = ("_width", "_height")
    width = PositiveNumber()
    height = PositiveNumber()

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


if __name__ == "__main__":
    # --- базовое поведение из заданий 39_01 / 39_02 ---
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print("Площадь круга:", circle.get_area())
    print("Площадь прямоугольника:", rectangle.get_area())

    try:
        Circle(-5)
    except InvalidSizeError as e:
        print("Ошибка:", e)

    try:
        Rectangle(3, 0)
    except InvalidSizeError as e:
        print("Ошибка:", e)

    print("\n--- Фабрика через реестр подклассов ---")
    s = Shape.create("circle", radius=3)
    print(s, "->", s.get_area())

    print("\n--- Сравнение и сортировка фигур по площади ---")
    shapes = [Circle(2), Rectangle(3, 3), Circle(1), Rectangle(10, 1)]
    for sh in sorted(shapes):
        print(f"{sh.__class__.__name__}: {sh.get_area():.2f}")
    print("Самая большая фигура:", repr(max(shapes)))
