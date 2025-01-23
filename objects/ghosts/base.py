import pyray as pr
import random
from objects.textures import Textures
# Объединенный класс для привидений
class Ghost:
    def __init__(self, x=0, y=0, direction=(0, 1), cell_size=10, color=pr.RED, field=None):
        self.__x = x
        self.__y = y
        self.cell_size = cell_size
        self.color = color
        self.direction = direction  # Используем direction вместо dx и dy
        self.speed = 1  # Увеличенная скорость привидения
        # TODO: замедлить призрака без проблем с коллизиями
        self.previous_directions = []  # Список предыдущих направлений
        self.field = field  # Поле для проверки столкновений
        self.textures = Textures()
        self.texture = None
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def choose_new_direction(self):
        # Получаем доступные направления
        possible_directions = GhostCrossDirectionChooser(self).get_possible_directions()
        # Исключаем последнее направление
        if self.previous_directions:
            last_direction = self.previous_directions[-1]
            possible_directions = [d for d in possible_directions if d != (-last_direction[0], -last_direction[1])]

        if possible_directions:
            new_direction = random.choice(possible_directions)
            self.set_direction(new_direction[0], new_direction[1])
            #print(f"Changed direction to: {self.direction}")
    def update(self):
        if self.direction != (0, 0):
            new_x = self.__x + self.direction[0] * self.speed
            new_y = self.__y + self.direction[1] * self.speed
            #print(f"new_x = {new_x}, new_y = {new_y}, direction = {self.direction}, can_move = {self.can_move(new_x, new_y)}")
            
            if self.can_move(new_x, new_y):
                self.__x = new_x
                self.__y = new_y
                #print(f"Moved to new position: ({self.__x}, {self.__y})")
                self.previous_directions.append(self.direction)  # Сохраняем текущее направление
            else:
                # Если не можем двигаться, проверяем, находимся ли на перекрестке
                if self.is_crossroad(int(self.__x), int(self.__y), self.field):
                    # Если на перекрестке, выбираем новое направление
                    direction_chooser = GhostCrossDirectionChooser(self)
                    direction_chooser.choose_direction()
                    #print(f"New direction chosen: {self.direction}")
                else:
                    # Если не на перекрестке, выбираем новое направление, избегая предыдущего
                    self.choose_new_direction()

            # Округляем координаты, если они близки к целым
            if (abs(self.__x % 1) < 0.001 and abs(self.__y % 1) < 0.001) or (abs(self.__x % 1) > 1- 0.001 and abs(self.__y % 1) >  1 - 0.001):
                self.__x = round(self.__x)
                self.__y = round(self.__y)
            if (self.__x == round(self.__x)) and (self.__y == round(self.__y)):
                # Проверка на портал
                if self.field[int(self.__y)][int(self.__x)] == 'T':
                    self.teleport()

    def can_move(self, new_x, new_y):
        int_x = int(new_x)
        int_y = int(new_y)
        return (0 <= int_x < len(self.field[0]) and 
                0 <= int_y < len(self.field) and 
                self.field[int_y][int_x] != '#')

    def teleport(self):
        """Телепортирует привидение в случайное место на карте."""
        valid_positions = [(x, y) for y in range(len(self.field)) for x in range(len(self.field[y]))
                        if self.field[y][x] == '_']
        if valid_positions:
            self.__x, self.__y = random.choice(valid_positions)

    def draw(self):
        # Определяем позицию для отрисовки текстуры
        draw_x = int(self.__x * self.cell_size)  # Приводим к int
        draw_y = int(self.__y * self.cell_size)  # Приводим к int
        # Отрисовываем текстуру
        if self.texture:
            pr.draw_texture(self.texture, draw_x, draw_y, pr.WHITE)

    def change_direction(self,field):
        #Проверяем, находится ли Ghost на перекрестке
        x = int(self.get_x())
        y = int(self.get_y())
        if self.is_crossroad(x, y, field):
            direction_chooser = GhostCrossDirectionChooser(self)
            direction_chooser.choose_direction()
            # print(f"Выбрано новое направление: {self.direction}")

    def set_direction(self, dx, dy):
        self.direction = (dx, dy)  # Устанавливаем direction как кортеж
# Класс для выбора направления привидения
class GhostWallDirectionChooser:
    def __init__(self, ghost: Ghost):
        self.ghost = ghost
        self.number_pixsels_in_cell_x = 10
        self.number_pixsels_in_cell_y = 10

    def dminus(self, d: tuple):
        x, y = d
        return (-y, x)

    def dplus(self, d: tuple):
        x, y = d
        return (y, -x)

class GhostCrossDirectionChooser:
    def __init__(self, ghost):
        self.ghost = ghost

    def get_possible_directions(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible_directions = []

        for dx, dy in directions:
            new_x = int(self.ghost.get_x() + dx)
            new_y = int(self.ghost.get_y() + dy)
            if self.ghost.can_move(new_x, new_y):
                possible_directions.append((dx, dy))

        return possible_directions

    def choose_direction(self):
        possible_directions = self.get_possible_directions()
        current_direction = self.ghost.direction  # Используем direction

        # Исключаем движение назад
        opposite_direction = (-current_direction[0], -current_direction[1])
        possible_directions = [d for d in possible_directions if d != opposite_direction]

        if possible_directions:
            new_direction = random.choice(possible_directions)
            self.ghost.set_direction(new_direction[0], new_direction[1])