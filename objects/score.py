import pyray as pr

class RecalculableText:
    def __init__(self, font_size=36):
        """Базовый класс для отображения изменяемого текста."""
        self.font_size = font_size

    def draw(self, text, position, color=pr.DARKGRAY):
        """Отображает текст на экране."""
        pr.draw_text(text, position[0], position[1], self.font_size, color)

class ScoreDrawer(RecalculableText):
    def __init__(self, x, y, score_counter):
        """
        Инициализирует объект для отрисовки количества очков.
        
        :param x: Координата x для отрисовки.
        :param y: Координата y для отрисовки.
        :param score_counter: Объект класса ScoreCounter, содержащий количество очков.
        """
        super().__init__()
        self.x = x
        self.y = y
        self.score_counter = score_counter

    def draw(self):
        """Отрисовывает количество очков на экране, используя сигнатуру из RecalculableText."""
        score_text = f'Score: {self.score_counter.get_score()}'
        super().draw(score_text, (self.x, self.y))
