import pyray as pr

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
    def __init__(self, x, y, texture):
        """
        Инициализирует объект для отрисовки количества жизней.
        
        :param x: Координата x для отрисовки.
        :param y: Координата y для отрисовки.
        :param score_counter: Объект класса ScoreCounter, содержащий количество жизней.
        """
        self.x = x
        self.y = y
        self.texture = texture
        super().__init__([self.x,self.y],self.texture)
    def draw(self,life_counts):
        """Отрисовывает количество жизней на экране, используя сигнатуру из RecalculableText."""
        super().draw(life_counts)