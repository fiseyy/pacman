import pyray
from objects.figure import Rect
import settings
class Pacman(Rect):
    def __init__(self, x, y, width=50, height=50, color=None, speed=5):
        super().__init__(x, y, width, height, pyray.YELLOW)
        self.speed = speed
        self.direction = None
        
    def move(self):
        if self.direction == 'up' and self._y > 0:
            self._y -= self.speed
        elif self.direction == 'down' and self._y + self._Rect__height < settings.Settings.HEIGHT:
            self._y += self.speed
        elif self.direction == 'left' and self._x > 0:
            self._x -= self.speed
        elif self.direction == 'right' and self._x + self._Rect__width < settings.Settings.WIDTH:
            self._x += self.speed
            
    def define_direction(self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_W):
            self.direction = 'up'
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_S):
            self.direction = 'down'
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_A):
            self.direction = 'left'
        elif pyray.is_key_pressed(pyray.KeyboardKey.KEY_D):
            self.direction = 'right'