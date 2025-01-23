from logic.field import Field
import pyray as pr
from objects.textures import Textures
from objects.images.seeds import Seed

class FieldDrawer:
    """
    Класс для отрисовки поля.

    Атрибуты:
        field (Field): Поле для отрисовки.
        cell_size (int): Размер ячейки.
        textures (Textures): Объект класса Textures для работы с текстурами.
        seeds (list): Список объектов Seed для хранения зёрен.
    """

    def __init__(self, field: Field, cell_size):
        """
        Инициализирует объект класса FieldDrawer.

        Аргументы:
            field (Field): Поле для отрисовки.
            cell_size (int): Размер ячейки.
        """
        self.field = field.load_field()
        self.cell_size = cell_size
        self.textures = Textures()
        self.seeds = []  # Список для хранения объектов Seed

        # Создаем зёрна и добавляем их в список
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell == '.':
                    seed = Seed(x, y, self.cell_size, self.textures.get_texture("seed"),weight=10)
                    self.seeds.append(seed)
                elif cell == 'S':
                    seed = Seed(x, y, self.cell_size, self.textures.get_texture("energizer"),weight=20)
                    self.seeds.append(seed)

    def draw(self, x_to_center=0, y_to_center=0):
        """
        Рисует поле.
        """
        for y, row in enumerate(self.field):
            for x, cell in enumerate(row):
                if cell == '#':
                    pr.draw_rectangle(x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, self.cell_size, self.cell_size, pr.BLUE)  # Стены
                elif cell == '_':
                    pr.draw_rectangle(x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, self.cell_size, self.cell_size, pr.BLACK)  # Пустые ячейки
                elif cell == 'D':
                    pr.draw_rectangle(x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, self.cell_size, self.cell_size, pr.BLACK)  # Декоративные ячейки
                elif cell in ('.', 'S'):
                    # Находим соответствующее зерно в списке и рисуем его
                    seed = next((s for s in self.seeds if s.x == x*self.cell_size and s.y == y*self.cell_size), None)
                    if seed:
                        seed.draw()
                elif cell == 'T':
                    pr.draw_rectangle(x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)