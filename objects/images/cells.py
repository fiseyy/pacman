import pygame

class Cell:
    COLORS = {
        0: (255, 255, 255),  # Белый - пустое место
        1: (0, 0, 0),        # Черный - стена
        2: (0, 0, 255),      # Синий - комната для призраков
        3: (0, 255, 0),      # Зеленый - телепорт
    }

    def __init__(self, cell_type, x, y, size):
        self.cell_type = cell_type
        self.x = x
        self.y = y
        self.size = size

    def render(self, screen):
        color = self.COLORS.get(self.cell_type, (255, 0, 0))
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))