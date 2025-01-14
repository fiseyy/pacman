import pyray
from objects.figure import Circle
import application
import settings

class Seed(Circle):
    """
    Класс малого зерна

    Args:
        x: Координата по х
        y: Координата по y
        radius: Радиус круга
        color: Цвет круга
        weight: Вес зерна, по умолчанию 10
    """
    def init(self, x, y, radius = 10, color=None, weight = 10):
        super().init(x, y, radius, pyray.YELLOW)
        self.weight = weight