import pyray as pr
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Pacman():
    def __init__(self, x, y, cell_size, textures, field):
        """Конструктор класса пакмана"""
        self.speed = 1  # скорость пакмана
        self.pos_x = x * cell_size  # абсолютное положение по горизонтали
        self.pos_y = y * cell_size  # абсолютное положение по вертикали
        self.__cell_size = cell_size  # сторона клетки (клетка - квадрат)
        self.pos_cell_x = x  # номер клетки
        self.pos_cell_y = y  # номер клетки
        self.textures = textures
        self.field = field
        self.texture = self.textures["right"]
        self.movement = PacmanMovement(self.pos_cell_x, self.pos_cell_y, (1, 0), self.field)
        self.changed_direction_on_crossroad = False
        self.teleported_to_portal = False
        self.future_direction = None  # Переменная для хранения будущего направления

    def draw(self):
        pr.draw_texture(self.texture, self.pos_x, self.pos_y, pr.WHITE)

    def move(self):
        # print(f"future {self.future_direction}, direction {self.movement.direction}") # DEBUG
        """Метод для передвижения пакмана в 4х направлениях"""
        if self.future_direction:
            # Устанавливаем текущее направление, если оно возможно
            if self.movement.can_move(self.future_direction) and self.pos_x % self.__cell_size == 0 and self.pos_y % self.__cell_size == 0 and not self.future_direction == self.movement.reverse_direction(self.movement.direction):
                self.movement.set_direction(self.future_direction)
            elif self.future_direction == self.movement.reverse_direction(self.movement.direction):
                self.movement.set_direction(self.future_direction)

        # Движение в текущем направлении
        if self.movement.can_move():
            self.pos_x += self.movement.get_direction()[0] * self.speed
            self.pos_y += self.movement.get_direction()[1] * self.speed

            # Обновляем позицию клетки
            if self.pos_x / self.__cell_size % 1 == 0 and self.pos_y / self.__cell_size % 1 == 0:
                self.pos_cell_x = int(self.pos_x / self.__cell_size)
                self.pos_cell_y = int(self.pos_y / self.__cell_size)
                self.movement.pos_cell_x = self.pos_cell_x
                self.movement.pos_cell_y = self.pos_cell_y

        # Проверка на портал
        if self.movement.is_portal():
            if not self.teleported_to_portal:
                portal_positions = self.movement.get_portal_positions()
                portal_positions.remove((self.pos_cell_x, self.pos_cell_y))  # Удаляем текущую позицию
                if portal_positions:  # Проверяем, есть ли доступные порталы
                    self.goto(portal_positions[0])  # Перемещаемся на первый доступный портал
                    self.teleported_to_portal = True
        else:
            self.teleported_to_portal = False  # Сбрасываем флаг, если не на портале

    def goto(self, target_cell_pos: tuple):
        """Перемещает Пакмана на целевую позицию"""
        target_cell_x, target_cell_y = target_cell_pos
        self.pos_cell_x = target_cell_x
        self.pos_cell_y = target_cell_y
        self.pos_x = self.pos_cell_x * self.__cell_size
        self.pos_y = self.pos_cell_y * self.__cell_size
        self.movement.pos_cell_x = self.pos_cell_x
        self.movement.pos_cell_y = self.pos_cell_y

    def define_direction(self):
        """Метод для определения направления движения клавишами WASD"""
        current_direction = self.movement.get_direction()

        if pr.is_key_down(pr.KeyboardKey.KEY_W) or pr.is_key_pressed(pr.KeyboardKey.KEY_W):  # Движение вверх
            self.future_direction = (0, -1)

        elif pr.is_key_down(pr.KeyboardKey.KEY_S) or pr.is_key_pressed(pr.KeyboardKey.KEY_S):  # Движение вниз
            self.future_direction = (0, 1)

        elif pr.is_key_down(pr.KeyboardKey.KEY_A) or pr.is_key_pressed(pr.KeyboardKey.KEY_A):  # Движение влево
            self.future_direction = (-1, 0)

        elif pr.is_key_down(pr.KeyboardKey.KEY_D) or pr.is_key_pressed(pr.KeyboardKey.KEY_D):  # Движение вправо
            self.future_direction = (1, 0)

    def can_turn(self, new_direction):
        """Проверяет, может ли Пакман повернуть в новое направление"""
        new_pos_x = self.pos_cell_x + new_direction[0]
        new_pos_y = self.pos_cell_y + new_direction[1]

        # Проверяем, находится ли новая позиция в пределах границ поля
        if new_pos_x < 0 or new_pos_x >= len(self.field.to_array()[0]) or new_pos_y < 0 or new_pos_y >= len(self.field.to_array()):
            return False  # Если новая позиция выходит за границы, поворот невозможен

        # Проверяем, есть ли препятствие в новой клетке
        if self.field.to_array()[new_pos_y][new_pos_x] == "#":
            return False  # Если есть коллизия, поворот невозможен

        return True  # Если коллизий нет, поворот возможен

class PacmanMovement:
    def __init__(self, pos_cell_x, pos_cell_y, direction, field):
        self.pos_cell_x = pos_cell_x
        self.pos_cell_y = pos_cell_y
        self.field = field  # поле (с методом get_array() для получения двумерного массива)
        self.direction = direction  # начальное направление

    def set_direction(self, direction):
        """Устанавливает новое направление движения."""
        self.direction = direction

    def get_direction(self):
        """Возвращает текущее направление движения."""
        return self.direction

    def can_move(self, direction=None):
        """Проверяет, можно ли двигаться в текущем направлении."""
        if direction is None:
            dx, dy = self.direction
        else:
            dx, dy = direction
        try:
            return self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#"
        except IndexError:
            return False

    def update_position(self):
        """Обновляет позицию пакмана на основе текущего направления."""
        dx, dy = self.direction
        if self.can_move():
            self.pos_cell_x += dx
            self.pos_cell_y += dy

    def is_portal(self):
        """Проверяет, находится ли пакман на портале."""
        return self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == "T"

    def get_portal_positions(self):
        """Возвращает список позиций порталов."""
        portal_positions = []
        for y in range(len(self.field)):  # Перебираем индексы строк
            for x in range(len(self.field[y])):  # Перебираем индексы столбцов
                if self.field.to_array()[x][y] == "T":  # Проверяем, есть ли "T" в текущей позиции
                    portal_positions.append((x, y))
        return portal_positions

    def reverse_direction(self, direction):
        return (-direction[0], -direction[1])