from objects.ghosts.base import Ghost, GhostCrossDirectionChooser
import pyray as pr

class InkyGhost(Ghost):
    def __init__(self, x=0, y=0, cell_size=10, field=None):
        super().__init__(x, y, field=field)
        self.ghosts_textures = self.textures.get_texture("inky")  # Получаем текстуру для Inky
        self.direction = (0, 1)  # Начальное направление (вниз)
        self.texture = self.ghosts_textures["down"]  # Текстура для Inky в зависимости от направления
        self.cell_size = cell_size

    def change_direction(self, field):
        # Проверяем, находится ли Inky на перекрестке
        super().change_direction(field)

    def is_crossroad(self, x, y, field):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for dx, dy in directions:
            if self.can_move(x + dx, y + dy):
                count += 1
        return count >= 3  # Перекресток, если 3 или 4 направления

    def update(self):
        super().update()

    def draw(self):
        # Устанавливаем текстуру в зависимости от направления
        if self.direction == (1, 0):
            self.texture = self.ghosts_textures["right"]
        elif self.direction == (-1, 0):
            self.texture = self.ghosts_textures["left"]
        elif self.direction == (0, 1):
            self.texture = self.ghosts_textures["down"]
        elif self.direction == (0, -1):
            self.texture = self.ghosts_textures["up"]

        super().draw()  # Вызываем метод draw родительского класса