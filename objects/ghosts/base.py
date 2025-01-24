import pyray as pr
import random
from objects.field import Field
# Привидения
class Ghost:
    def __init__(self,x=0,y=0,cell_size=10, direction=(0,1), field:Field=None, textures=None):
        self.pos_x = x * cell_size # координата по горизонтали (x)
        self.pos_y = y * cell_size # координата по вертикали (y)
        self.__cell_size = cell_size
        self.pos_cell_x = x # номер клетки
        self.pos_cell_y = y
        self.speed = 1
        self.movement = GhostMovement(self.pos_cell_x, self.pos_cell_y, direction, field) # направление движения
        self.textures = textures # предпологается, что взят не весь кортеж текстур, а только нужного призрака
        self.texture = None # текущая текстура в зависимости от направления
        self.field = field # предпологается, что поле не пустое
        self.changed_direction_on_crossroad = False
        self.teleported_to_portal = False
    def update(self):
        # движение в зависимости от direction и свободных клеток слева/справа
        # print(self.direction.can_move(), self.direction.get_direction())  # DEBUG PRINT
        # print(self.movement.can_move(), self.movement.get_direction()) # DEBUG PRINT
        if not self.movement.is_crossroad() and not self.movement.is_portal():
            self.changed_direction_on_crossroad = False
            self.teleported_to_portal = False
            if self.movement.can_move():
                self.pos_x += self.movement.get_direction()[0] * self.speed
                self.pos_y += self.movement.get_direction()[1] * self.speed

                # if isinstance(self.pos_x/self.__cell_size, int):
                if self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0:
                    #DEBUG PRINT
                    #print(self.pos_x, self.pos_y, self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0, self.pos_x/self.__cell_size, self.pos_y/self.__cell_size)
                    # можно заменять pos_cell_x и pos_cell_y
                    self.pos_cell_x = int(self.pos_x / self.__cell_size)
                    self.pos_cell_y = int(self.pos_y / self.__cell_size)
                    # также поменяем в direction
                    self.movement.pos_cell_x = self.pos_cell_x
                    self.movement.pos_cell_y = self.pos_cell_y
            else:
                self.movement.choose_new_direction()
        elif self.movement.is_crossroad():
            if not self.changed_direction_on_crossroad:
                self.movement.choose_new_direction()
                self.changed_direction_on_crossroad = True
            else:
                if self.movement.can_move():
                    self.pos_x += self.movement.get_direction()[0] * self.speed
                    self.pos_y += self.movement.get_direction()[1] * self.speed
                    # if isinstance(self.pos_x/self.__cell_size, int):
                    if self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0:
                        #DEBUG PRINT
                        #print(self.pos_x, self.pos_y, self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0, self.pos_x/self.__cell_size, self.pos_y/self.__cell_size)
                        # можно заменять pos_cell_x и pos_cell_y
                        self.pos_cell_x = int(self.pos_x / self.__cell_size)
                        self.pos_cell_y = int(self.pos_y / self.__cell_size)
                        # также поменяем в direction
                        self.movement.pos_cell_x = self.pos_cell_x
                        self.movement.pos_cell_y = self.pos_cell_y
        elif self.movement.is_portal():
            if not self.teleported_to_portal:
                portal_positions = self.movement.get_portal_positions()
                print(portal_positions)
                portal_positions.remove((self.pos_cell_x, self.pos_cell_y))
                self.goto(portal_positions[0])
                self.teleported_to_portal = True
            else:
                if self.movement.can_move():
                    self.pos_x += self.movement.get_direction()[0] * self.speed
                    self.pos_y += self.movement.get_direction()[1] * self.speed
                    # if isinstance(self.pos_x/self.__cell_size, int):
                    if self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0:
                        #DEBUG PRINT
                        #print(self.pos_x, self.pos_y, self.pos_x/self.__cell_size % 1 == 0 and self.pos_y/self.__cell_size % 1 == 0, self.pos_x/self.__cell_size, self.pos_y/self.__cell_size)
                        # можно заменять pos_cell_x и pos_cell_y
                        self.pos_cell_x = int(self.pos_x / self.__cell_size)
                        self.pos_cell_y = int(self.pos_y / self.__cell_size)
                        # также поменяем в direction
                        self.movement.pos_cell_x = self.pos_cell_x
                        self.movement.pos_cell_y = self.pos_cell_y
    def draw(self):
        #взятие нужной модели
        if self.movement.get_direction() == (1, 0):
            self.texture = self.textures["right"]
        elif self.movement.get_direction() == (-1, 0):
            self.texture = self.textures["left"]
        elif self.movement.get_direction() == (0, 1):
            self.texture = self.textures["down"]
        elif self.movement.get_direction() == (0, -1):
            self.texture = self.textures["up"]
        else:
            self.texture = self.textures["right"]
        # отрисовка на нужной координате
        pr.draw_texture(self.texture, self.pos_x-2, self.pos_y-2, pr.WHITE)
    def goto(self,target_cell_pos: tuple):
        target_cell_x = target_cell_pos[0]
        target_cell_y = target_cell_pos[1]
        self.pos_cell_x = target_cell_x
        self.pos_cell_y = target_cell_y
        self.pos_x = self.pos_cell_x * self.__cell_size
        self.pos_y = self.pos_cell_y * self.__cell_size
        self.movement.pos_cell_x = self.pos_cell_x
        self.movement.pos_cell_y = self.pos_cell_y
    
class GhostMovement:
    def __init__(self, pos_cell_x, pos_cell_y, direction, field):
        self.pos_cell_x = pos_cell_x
        self.pos_cell_y = pos_cell_y
        self.direction = direction # кортеж
        self.field = field # поле (двумерный массив)
    def choose_new_direction(self):
        self.previous_direction = self.direction
        self.possible_directions:list = self.get_possible_directions()
        if not self.is_crossroad():
            for possible_direction in self.possible_directions:
                if possible_direction != self.reverse_direction(self.previous_direction):
                    self.direction = possible_direction
        else:
            for possible_direction in self.possible_directions:
                if possible_direction == self.reverse_direction(self.previous_direction):
                    self.possible_directions.remove(possible_direction)
            self.direction = random.choice(self.possible_directions)
        return self.direction
    def get_direction(self):
        return self.direction
    def set_direction(self, direction):
        self.direction = direction
    def get_portal_positions(self):
        portal_positions = []
        for y in range(len(self.field)):  # Перебираем индексы строк
            for x in range(len(self.field[y])):  # Перебираем индексы столбцов
                if self.field.to_array()[x][y] == "T":  # Проверяем, есть ли "T" в текущей позиции
                    portal_positions.append((x, y))
        return portal_positions
  
    def get_possible_directions(self):
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]
        possible_directions = []
        for dx, dy in directions:
            if self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#":
                possible_directions.append((dx,dy))
        return possible_directions
    def can_move(self, dx = None, dy = None):
        if dx is None:
            dx = self.direction[0]
        if dy is None:
            dy = self.direction[1]
        #print(self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy])
        # Field.to_array() возвращает list с list'ами
        try:
            if self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#":
                return True
        except IndexError:
            return False
        return False
    
    def is_crossroad(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for dx, dy in directions:
            if self.can_move(dx, dy):
                count += 1
        #print(f"directions = {count}")
        return count >= 3  # Перекресток, если 3 или 4 направления
    def is_portal(self):
        return self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == "T"
    def reverse_direction(self, direction):
        return (-direction[0], -direction[1])
    