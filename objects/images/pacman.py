import pyray as pr
import settings
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
class Pacman():
    """
    Класс пакмана, представлен в виде прямоугольника

    Args:
        x: Координата по х
        y: Координата по y
        width: Ширина прямоугольника
        height: Высота прямоугольника
        color: Цвет прямоугольника
        speed: Скорость передвижения
        
    Methods:
        move(): Метод для передвижения пакмана в 4х направлениях
        define_direction(): Метод для определения направления движения клавишами WASD
    """
    def __init__(self, x, y, cell_size, textures):
        self.speed = 1 # скорость пакмана
        self.direction = None
        self._x = x*cell_size # номер клетки по горизонтали
        self._y = y*cell_size # номер клетки по вертикали
        self.cell_size = cell_size # сторона клетки (клетка - квадрат)
        self.textures = textures
        self.texture = self.textures["right"]
    def draw(self):
        pr.draw_texture(self.texture, self._x, self._y, pr.WHITE)
    def move(self):
        """
        Метод для передвижения пакмана в 4х направлениях
        """
        if self.direction == 'up' and self._y > 0:
            self._y -= self.speed
        elif self.direction == 'down' and self._y +  self.cell_size < SCREEN_HEIGHT:
            self._y += self.speed
        elif self.direction == 'left' and self._x > 0:
            self._x -= self.speed
        elif self.direction == 'right' and self._x + self.cell_size < SCREEN_WIDTH:
            self._x += self.speed
            
    def define_direction(self):
        """
        Метод для определения направления движения клавишами WASD
        """
        if pr.is_key_down(pr.KeyboardKey.KEY_W):
            self.direction = 'up'
        elif pr.is_key_down(pr.KeyboardKey.KEY_S):
            self.direction = 'down'
        elif pr.is_key_down(pr.KeyboardKey.KEY_A):
            self.direction = 'left'
        elif pr.is_key_down(pr.KeyboardKey.KEY_D):
            self.direction = 'right'