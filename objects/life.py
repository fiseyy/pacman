import pygame as pr

class LifeCounter:
    def __init__(self, initial_lives=3):
        """
        Инициализирует счётчик жизней с заданным количеством жизней.
        
        :param initial_lives: Начальное количество жизней (по умолчанию 3).
        """
        self.lives = initial_lives

    def add(self):
        """Увеличивает количество жизней на 1."""
        self.lives += 1

    def remove(self):
        """Уменьшает количество жизней на 1, если они больше 0."""
        if self.lives > 0:
            self.lives -= 1

    def get_lives(self):
        """Возвращает текущее количество жизней."""
        return self.lives

class LifeDrawer:
    def __init__(self, x, y, life_counter):
        """
        Инициализирует объект для отрисовки количества жизней.
        
        :param x: Координата x для отрисовки.
        :param y: Координата y для отрисовки.
        :param life_counter: Объект класса LifeCounter, содержащий количество жизней.
        """
        self.x = x
        self.y = y
        self.life_counter = life_counter

    def draw(self, screen):
        """
        Отрисовывает количество жизней в виде жёлтых кругов на экране.
        
        :param screen: Объект экрана для отрисовки.
        """
        for i in range(self.life_counter.get_lives()):
            # Отрисовка жёлтого круга радиусом 10 пикселей
            pr.draw.circle(screen, pr.Color('yellow'), (self.x + i * 30, self.y), 10)

def main():
    # Инициализация Pygame
    pr.init()
    screen = pr.display.set_mode((800, 600))
    pr.display.set_caption("Life Counter Example Pacman")

    # Создание объектов LifeCounter и LifeDrawer
    life_counter = LifeCounter(initial_lives=3)
    life_drawer = LifeDrawer(50, 50, life_counter)

    running = True
    while running:
        for event in pr.event.get():
            if event.type == pr.QUIT:
                running = False
            elif event.type == pr.KEYDOWN:
                if event.key == pr.K_f:
                    # Уменьшение количества жизней при нажатии на 'F'
                    life_counter.remove()

        screen.fill((0, 0, 0))  # Очистка экрана (черный фон)
        life_drawer.draw(screen)  # Отрисовка жизней

        pr.display.flip()  # Обновление экрана

    pr.quit()

if __name__ == "__main__":
    main()