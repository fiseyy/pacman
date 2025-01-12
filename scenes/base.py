import pyray as pr
from settings import font
# Базовый класс для сцен
class SceneBase:
    """
    Базовый класс для всех сцен.

    Методы:
        enter(): Входит в сцену.
        exit(): Выходит из сцены.
        update(): Обновляет сцену.
        draw(): Рисует сцену.
    """

    def enter(self):
        """
        Входит в сцену.
        """
        pass

    def exit(self):
        """
        Выходит из сцены.
        """
        pass

    def update(self):
        """
        Обновляет сцену.
        """
        pass

    def draw(self):
        """
        Рисует сцену.
        """
        pass
