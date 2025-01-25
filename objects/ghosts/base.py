import pyray as pr
import random
from objects.field import Field
# Привидения
class Ghost:
    def __init__(self,x=0,y=0,cell_size=10, direction=(0,-1), field:Field=None, textures=None, time_to_movement_since_start=5):
        self.__cell_size = cell_size
        self.speed = 1
        self.time_to_movement_since_start = time_to_movement_since_start
        self.field = field # предпологается, что поле не пустое
        self.spawned = False
        self.died = False
        self.afraid = False
        self.died_time_end = None
        self.init_direction = direction # направление движения
        self.textures = textures # предпологается, что взят не весь кортеж текстур, а только нужного призрака
        self.spawn()
    def spawn(self):
        free_spawners = self.field.ghost_spawners.get_free_spawn_locations()
        spawn = random.choice(free_spawners) # tuple(x,y)
        self.field.ghost_spawners.occupy_spawn_location(spawn)
        self.pos_x = spawn[0] * self.__cell_size # координата по горизонтали (x)
        self.pos_y = spawn[1] * self.__cell_size # координата по вертикали (y)
        self.pos_cell_x = spawn[0] # номер клетки
        self.pos_cell_y = spawn[1]
        self.spawn_cell_x = self.pos_cell_x
        self.spawn_cell_y = self.pos_cell_y
        # ждать 5 сек
        self.spawn_time = pr.get_time()
        self.movement = GhostMovement(self.pos_x, self.pos_y, self.pos_cell_x, self.pos_cell_y, self.init_direction, self.field, self) # направление движения
        self.texture = None # текущая текстура в зависимости от направления
        self.changed_direction_on_crossroad = False
        self.teleported_to_portal = False
        self.spawned = True
    def update(self):
        if self.died_time_end != None:
                self.goto(tuple((self.spawn_cell_x, self.spawn_cell_y)))
                if self.died_time_end < pr.get_time():
                    self.died_time_end = None
                    self.died = False
                    self.afraid = False
        if self.afraid:
            if not self.pacman.turn_to_blue:
                self.afraid = False
        if self.spawned and (pr.get_time() - self.spawn_time >= self.time_to_movement_since_start) and not self.died:
            # движение в зависимости от direction и свободных клеток слева/справа
            # print(self.direction.can_move(), self.direction.get_direction())  # DEBUG PRINT
            # print(self.movement.can_move(), self.movement.get_direction()) # DEBUG PRINT
            # debug_msg = f"can_move = {self.movement.can_move()}, direction = {self.movement.direction}, pos = {self.pos_cell_x}, {self.pos_cell_y}, crossroad = {self.movement.is_crossroad()}, portal = {self.movement.is_portal()}"
            # print(debug_msg)
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
                    self.change_direction()
            elif self.movement.is_crossroad():
                if not self.changed_direction_on_crossroad:
                    self.change_direction()
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
                    else: 
                        self.change_direction()
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
        if self.spawned:
            #взятие нужной модели
            if not self.afraid and not self.died:
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
            elif self.died:
                self.texture = self.textures["died"]
            elif self.afraid:
                self.texture = self.textures["afraid"]
            # отрисовка на нужной координате
            pr.draw_texture(self.texture, self.pos_x-2, self.pos_y-2, pr.WHITE)
    def goto(self,target_cell_pos: tuple):
        if self.spawned:
            target_cell_x = target_cell_pos[0]
            target_cell_y = target_cell_pos[1]
            self.pos_cell_x = target_cell_x
            self.pos_cell_y = target_cell_y
            self.pos_x = self.pos_cell_x * self.__cell_size
            self.pos_y = self.pos_cell_y * self.__cell_size
            self.movement.pos_cell_x = self.pos_cell_x
            self.movement.pos_cell_y = self.pos_cell_y
    def change_direction(self):
        self.movement.choose_new_direction()
        
class GhostMovement:
    def __init__(self, x, y, pos_cell_x, pos_cell_y, direction, field, ghost):
        self.pos_x = x  # координата x
        self.pos_y = y # координата y
        self.pos_cell_x = pos_cell_x
        self.pos_cell_y = pos_cell_y
        self.direction = direction # кортеж
        self.field = field  # поле (с методом get_array() для получения двумерного массива)
        self.ghost = ghost
    def set_direction_based_on_target(self, target_x, target_y):
        # Определяем направление к Пакману
        dx = target_x - self.pos_cell_x
        dy = target_y - self.pos_cell_y

        # Нормализуем направление
        if abs(dx) > abs(dy):
            if dx > 0:
                new_direction = (1, 0)  # Двигаться вправо
            else:
                new_direction = (-1, 0)  # Двигаться влево
        else:
            if dy > 0:
                new_direction = (0, 1)  # Двигаться вниз
            else:
                new_direction = (0, -1)  # Двигаться вверх

        # Проверяем, можем ли мы двигаться в этом направлении
        if self.can_move(new_direction[0], new_direction[1]):
            self.set_direction(new_direction)
    def is_moving(self)->bool:
        return self.direction != (0, 0)
    
    def choose_direction_away_from(self, target_x, target_y):
        # Определяем направление от Пакмана
        dx = self.pos_cell_x - target_x
        dy = self.pos_cell_y - target_y

        # Нормализуем направление
        if abs(dx) > abs(dy):
            if dx > 0:
                new_direction = (1, 0)  # Двигаться вправо
            else:
                new_direction = (-1, 0)  # Двигаться влево
        else:
            if dy > 0:
                new_direction = (0, 1)  # Двигаться вниз
            else:
                new_direction = (0, -1)  # Двигаться вверх

        # Проверяем, можем ли мы двигаться в этом направлении
        if self.can_move(*new_direction):
            self.set_direction(new_direction)
        else:
            # Если не можем двигаться в этом направлении, выбираем другое направление
            self.choose_new_direction()
    def check_collision_with_pacman(self,pacman):
        if pacman.pos_cell_x == self.pos_cell_x and pacman.pos_cell_y == self.pos_cell_y:
            return True
        return False
    def choose_new_direction(self):
        self.previous_direction = self.direction
        self.possible_directions:list = self.get_possible_directions()
        if not self.is_crossroad():
            for possible_direction in self.possible_directions:
                if possible_direction != self.reverse_direction(self.previous_direction):
                    self.direction = possible_direction
        else:
            # for possible_direction in self.possible_directions:
                # if possible_direction == self.reverse_direction(self.previous_direction):
                #     self.possible_directions.remove(possible_direction)
            print(self.possible_directions)
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
            if (self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#") and (self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "Z"):
                possible_directions.append((dx,dy))
        return possible_directions
    def can_move(self, dx = None, dy = None):
        if dx is None:
            if not len(self.direction) == 0:
                dx = self.direction[0]
            else:
                return False
        if dy is None:
            if not len(self.direction) == 0:
                dy = self.direction[1]
            else:
                return False
        #print(self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy])
        # Field.to_array() возвращает list с list'ами
        try:
            if (self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#") and (self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "Z"):
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
        if not len(direction) == 0:
            return (-direction[0], -direction[1])
        return (0,0)
    def died(self):
        if not self.ghost.died:
            self.ghost.died = True
            self.ghost.died_time_end = pr.get_time() + 10
            self.ghost.draw()