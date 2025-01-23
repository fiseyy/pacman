import pygame as pr

class ScoreCounter:
    def __init__(self, initial_score=0):
        """Инициализирует счётчик очков с заданным начальным значением."""
        self.score = initial_score

    def add(self, points):
        """Увеличивает количество очков на заданное значение."""
        self.score += points

    def remove(self, points):
        """Уменьшает количество очков на заданное значение, если это возможно."""
        if self.score >= points:
            self.score -= points
        else:
            self.score = 0

    def get_score(self):
        """Возвращает текущее количество очков."""
        return self.score

class RecalculableText:
    def __init__(self, font_size=36):
        """Базовый класс для отображения изменяемого текста."""
        self.font = pr.font.Font(None, font_size)

    def draw(self, screen, text="", position=(0, 0), color=(255, 255, 255)):
        """Отображает текст на экране."""
        rendered_text = self.font.render(text, True, color)
        screen.blit(rendered_text, position)

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

    def draw(self, screen):
        """Отрисовывает количество очков на экране, используя сигнатуру из RecalculableText."""
        score_text = f'Score: {self.score_counter.get_score()}'
        super().draw(screen, text=score_text, position=(self.x, self.y))

def main():
    # Инициализация Pygame
    pr.init()
    screen = pr.display.set_mode((800, 600))
    pr.display.set_caption("Score Counter Example")

    # Создание объектов ScoreCounter и ScoreDrawer
    score_counter = ScoreCounter(initial_score=0)
    score_drawer = ScoreDrawer(50, 100, score_counter)

    running = True
    while running:
        for event in pr.event.get():
            if event.type == pr.QUIT:
                running = False
            elif event.type == pr.KEYDOWN:
                if event.key == pr.K_UP:
                    score_counter.add(10)
                elif event.key == pr.K_DOWN:
                    score_counter.remove(5)

        screen.fill((0, 0, 0))  # Очистка экрана (черный фон)
        score_drawer.draw(screen)  # Отрисовка очков

        pr.display.flip()  # Обновление экрана

    pr.quit()

if __name__ == "__main__":
    main()