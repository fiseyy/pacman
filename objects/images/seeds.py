import pyray as pr


class Seed:
    """
    Класс малого зерна

    Args:
        x: Координата по х
        y: Координата по y
        radius: Радиус круга, по умолчанию 10
        weight: Вес зерна, по умолчанию 10
    """
    def __init__(self, x, y, cell_size, texture, weight = 10, radius = 10):
        self.weight = weight
        self.x = x * cell_size # номер клетки по X
        self.y = y * cell_size # номер клетки по Y
        self.radius = radius
        self.texture = texture
        self.cell_size = cell_size
    def draw(self):
        pr.draw_texture(self.texture, self.x, self.y, pr.WHITE)
    def collisions(self, pacman: pr.Rectangle):
        # TODO: Добавить проверку на коллизию с Pacman
        pass
    def hide(self):
        pass