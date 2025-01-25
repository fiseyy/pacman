import pyray as pr
from objects.images.pacman import Pacman
from logic.score import ScoreCounter
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
        self.x = x * cell_size # абсолютный X
        self.y = y * cell_size # абсолютный Y
        self.pos_cell_x = x # номер клетки по X
        self.pos_cell_y = y # номер клетки по Y
        self.radius = radius
        self.texture = texture
        self.cell_size = cell_size
        self.hidden = False

    def draw(self):
        if not self.hidden:
            pr.draw_texture(self.texture, self.x, self.y, pr.WHITE)
            
    def collisions(self,pacman: Pacman, score_counter: ScoreCounter):
        if not self.hidden:
            if pacman.pos_cell_x == self.pos_cell_x and pacman.pos_cell_y == self.pos_cell_y:
                self.hide()
                pacman.collision.which_collision()
                score_counter.add(self.weight)
            
    def hide(self):
        self.hidden = True
