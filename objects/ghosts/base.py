import pyray as pr
import random
# Базовый класс для привидений
class Ghost:
    def __init__(self, x, y, cell_size, color, field_matrix):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color
        self.dx = 0
        self.dy = 0
        self.speed = 0.15  # Увеличенная скорость привидения
        self.previous_directions = []  # Список предыдущих направлений
        self.field_matrix = field_matrix  # Матрица для проверки на портал
    def update(self):
        if self.dx != 0 or self.dy != 0:
            new_x = self.x + self.dx * self.speed
            new_y = self.y + self.dy * self.speed
            
            if self.can_move(new_x, new_y):
                self.x = new_x
                self.y = new_y
            
            if abs(self.x % 1) < self.speed and abs(self.y % 1) < self.speed:
                self.x = round(self.x)
                self.y = round(self.y)
                self.dx, self.dy = 0, 0

                # Проверка на портал
                if self.field_matrix[int(self.y)][int(self.x)] == 'T':
                    self.teleport()

        else:
            self.choose_direction()

    def can_move(self, new_x, new_y):
        int_x = int(new_x)
        int_y = int(new_y)
        return (0 <= int_x < len(self.field_matrix[0]) and 
                0 <= int_y < len(self.field_matrix) and 
                self.field_matrix[int_y][int_x] != '#')

    def teleport(self):
        """Телепортирует привидение в случайное место на карте."""
        valid_positions = [(x, y) for y in range(len(self.field_matrix)) for x in range(len(self.field_matrix[0]))
                           if self.field_matrix[y][x] == '_']
        if valid_positions:
            self.x, self.y = random.choice(valid_positions)

    def draw(self):
        x1 = self.x * self.cell_size + self.cell_size // 2
        y1 = self.y * self.cell_size
        x2 = self.x * self.cell_size
        y2 = self.y * self.cell_size + self.cell_size
        x3 = self.x * self.cell_size + self.cell_size
        y3 = self.y * self.cell_size + self.cell_size
        vertices = [(x1, y1), (x2, y2), (x3, y3)]
        pr.draw_triangle(vertices[0], vertices[1], vertices[2], self.color)

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def choose_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        
        for new_dx, new_dy in directions:
            new_x = self.x + new_dx
            new_y = self.y + new_dy
            
            if self.can_move(new_x, new_y) and (new_dx, new_dy) not in self.previous_directions:
                self.set_direction(new_dx, new_dy)
                self.previous_directions.append((new_dx, new_dy))
                break
        
        if len(self.previous_directions) > 10:
            self.previous_directions.pop(0)

