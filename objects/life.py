import pyray as pr

class RecalculableText:
    def __init__(self, font_size=36):
        """Базовый класс для отображения изменяемого текста."""
        self.font_size = font_size

    def draw(self, text, position, color=pr.DARKGRAY):
        """Отображает текст на экране."""
        pr.draw_text(text, position[0], position[1], self.font_size, color)

class LifeDrawer(RecalculableText):
    def __init__(self, x, y, life_counter):
        """
        Инициализирует объект для отрисовки количества жизней.
        
        :param x: Координата x для отрисовки.
        :param y: Координата y для отрисовки.
        :param score_counter: Объект класса ScoreCounter, содержащий количество жизней.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.life_counter = life_counter

    def draw(self):
        """Отрисовывает количество жизней на экране, используя сигнатуру из RecalculableText."""
        life_text = f'Lifes: {self.life_counter.get_lives()}'
        super().draw(life_text, (self.x, self.y))
