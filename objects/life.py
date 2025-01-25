import pyray as pr
from logic.life import LifeCounter
class DrawHearts:
    def __init__(self, position, texture):
        self.position = position
        self.texture = texture

    def draw(self, life_count):
        current_position = list(self.position)  # Создаем новый список для текущей позиции
        for _ in range(life_count):
            pr.draw_texture(self.texture, current_position[0], current_position[1], pr.WHITE)
            current_position[0] += 30  # Сдвигаем позицию для следующего сердца

class LifeDrawer(DrawHearts):
    def __init__(self, x, y, texture,LifeCounter_obj):
        """
        Инициализирует объект для отрисовки количества жизней.
        
        :param x: Координата x для отрисовки.
        :param y: Координата y для отрисовки.
        :param score_counter: Объект класса ScoreCounter, содержащий количество жизней.
        """
        self.LifeCounter_obj=LifeCounter_obj
        self.x = x
        self.y = y
        self.texture = texture
        self.life_counts=LifeCounter_obj.get_lives()
        super().__init__([self.x,self.y],self.texture)
    def draw(self):
        """Отрисовывает количество жизней на экране, используя сигнатуру из RecalculableText."""
        super().draw(self.life_counts)