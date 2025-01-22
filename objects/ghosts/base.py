import pyray as pr
import random
from logic.field import Field

# Класс для преобразования изображений в текстуры
class Textures:
    def __init__(self):
        self.seed = pr.load_texture_from_image(pr.load_image("images/corn_1.png")) # текстура малого зерна
        self.energizer = pr.load_texture_from_image(pr.load_image("images/corn_2.png")) # текстура большого зерна
        self.textures={
            "seed": self.seed,
            "energizer": self.energizer
        }
    def get_texture(self, texture_name):
        return self.textures[texture_name]
    def unload(self):
        pr.unload_texture(self.seed)
        pr.unload_texture(self.energizer)

# Класс для отрисовки поля
class FieldDrawer:
    def __init__(self, field:Field, cell_size):
        self.field = field.load_field()
        self.cell_size = cell_size
        self.textures = Textures()
    def draw(self):
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell == '#':
                    pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.BLUE)  # Стены
                elif cell == '_':
                    pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.BLACK)  # Пустые ячейки
                elif cell == '.':
                    # малое зерно
                    texture = self.textures.get_texture("seed")
                    pr.draw_texture(texture, x * self.cell_size,y * self.cell_size,pr.WHITE)
                    #pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)
                elif cell == 'S':
                    # большое зерно
                    texture = self.textures.get_texture("energizer")
                    pr.draw_texture(texture, x * self.cell_size,y * self.cell_size,pr.WHITE)
                    # pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)
                elif cell == 'T':
                    pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)  # Порталы

# Объединенный класс для привидений
class Ghost:
    def __init__(self, x=0, y=0, direction=(0, 1), cell_size=10, color=pr.RED, field=None):
        self.__x = x
        self.__y = y
        self.cell_size = cell_size
        self.color = color
        self.dx = 0
        self.dy = 0
        self.speed = 0.15  # Увеличенная скорость привидения
        self.previous_directions = []  # Список предыдущих направлений
        self.direction = direction
        self.field = field  # Поле для проверки столкновений

    def update(self):
        if self.dx != 0 or self.dy != 0:
            new_x = self.__x + self.dx * self.speed
            new_y = self.__y + self.dy * self.speed
            
            if self.can_move(new_x, new_y):
                self.__x = new_x
                self.__y = new_y
            
            if abs(self.__x % 1) < self.speed and abs(self.__y % 1) < self.speed:
                self.__x = round(self.__x)
                self.__y = round(self.__y)
                self.dx, self.dy = 0, 0

                # Проверка на портал
                if self.field[int(self.__y)][int(self.__x)] == 'T':
                    self.teleport()

        else:
            self.choose_direction()

    def can_move(self, new_x, new_y):
        int_x = int(new_x)
        int_y = int(new_y)
        return (0 <= int_x < len(self.field[0]) and 
                0 <= int_y < len(self.field) and 
                self.field[int_y][int_x] != '#')

    def teleport(self):
        """Телепортирует привидение в случайное место на карте."""
        valid_positions = [(x, y) for y in range(len(self.field)) for x in range(len(self.field[0]))
                           if self.field[y][x] == '_']
        if valid_positions:
            self.__x, self.__y = random.choice(valid_positions)

    def draw(self):
        x1 = self.__x * self.cell_size + self.cell_size // 2
        y1 = self.__y * self.cell_size
        x2 = self.__x * self.cell_size
        y2 = self.__y * self.cell_size + self.cell_size
        x3 = self.__x * self.cell_size + self.cell_size
        y3 = self.__y * self.cell_size + self.cell_size
        vertices = [(x1, y1), (x2, y2), (x3, y3)]
        pr.draw_triangle(vertices[0], vertices[1], vertices[2], self.color)

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def choose_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for new_dx, new_dy in directions:
            new_x = self.__x + new_dx
            new_y = self.__y + new_dy
            
            if self.can_move(new_x, new_y) and (new_dx, new_dy) not in self.previous_directions:
                self.set_direction(new_dx, new_dy)
                self.previous_directions.append((new_dx, new_dy))
                break
        
        if len(self.previous_directions) > 10:
            self.previous_directions.pop(0)

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

    def change_direction(self):
        x = self.ghost.get_x() // self.number_pixsels_in_cell_x
        y = self.ghost.get_y() // self.number_pixsels_in_cell_y
        direction = self.ghost.get_direction()

        if self.ghost.field[x + direction[0]][y + direction[1]] == "#":
            if self.ghost.field[self.dminus(direction)[0]][self.dminus(direction)[1]] == "#":
                if self.ghost.field[self.dplus(direction)[0]][self.dplus(direction)[1]] == "#":
                    self.ghost.set_direction((-direction[0], -direction[1]))
                else:
                    self.ghost.set_direction(self.dminus(direction))
            elif self.ghost.field[self.dplus(direction)[0]][self.dplus(direction)[1]] == "#":
                self.ghost.set_direction(self.dminus(direction))
            else:
                self.ghost.set_direction(self.dminus(direction))

# Пример запуска
# if __name__ == "__main__":
#     field = Field("C:\\git\\pacman-rl-2-group\\logic\\field.txt")
#     field_drawer = FieldDrawer(field,20)
