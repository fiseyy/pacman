import pyray
from raylib import colors
from objects.base import BaseObject


class Rect(BaseObject):
    def __init__(self, x, y, width, height, color=None, outline=False):
        """
        Класс прямоугольника Raylib.
        """
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color if color else colors.RED
        self.__outline = outline

    def set_size(self, w, h):
        self.__width = w
        self.__height = h

    def draw(self):
        draw_func = pyray.draw_rectangle if not self.__outline else pyray.draw_rectangle_lines
        draw_func(self._x, self._y, self.__width, self.__height, self.__color)


class Circle(BaseObject):
    def __init__(self, x, y, radius, color=None, outline=False):
        """
        Класс круга Raylib.
        """
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color if color else colors.RED
        self.__outline = outline

    def resize(self, radius):
        """
        Меняет радиус круга
        """
        self.__radius = radius

    def set_color(self, color):
        """
        Устанавливает цвет круга
        """
        self.__color = color

    def draw(self):
        draw_func = pyray.draw_circle if not self.__outline else pyray.draw_circle_lines
        draw_func(self._x, self._y, self.__radius, self.__color)


class Ellipse(BaseObject):
    def __init__(self, x, y, radius_w, radius_h, color=None, outline=False):
        """
        Класс эллипса Raylib.
        """
        super().__init__(x, y)
        self.__radius_w = radius_w
        self.__radius_h = radius_h
        self.__color = color if color else colors.RED
        self.__outline = outline

    def resize(self, radius_w, radius_h):
        """
        Меняет радиус эллипса
        """
        self.__radius_w = radius_w
        self.__radius_h = radius_h

    def set_color(self, color):
        """
        Устанавливает цвет эллипса
        """
        self.__color = color

    def draw(self):
        draw_func = pyray.draw_ellipse if not self.__outline else pyray.draw_ellipse_lines
        draw_func(self._x, self._y, self.__radius_w, self.__radius_h, self.__color)
