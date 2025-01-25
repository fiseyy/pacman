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
    def __init__(self, x, y, cell_size, texture, pacman, weight = 10, radius = 10):
        self.weight = weight
        self.x = x * cell_size # номер клетки по X
        self.y = y * cell_size # номер клетки по Y
        self.radius = radius
        self.texture = texture
        self.cell_size = cell_size
        self.hidden = False
        self.pacman = pacman

    def draw(self):
        if not self.hidden:
            pr.draw_texture(self.texture, self.x, self.y, pr.WHITE)
            
    def collisions(self):
        if self.pacman.pos_cell_x == self.x and self.pacman.pos_cell_y == self.y:
            self.hide()
            self.pacman.collision.which_collision()
            
    def hide(self):
        self.hidden = True