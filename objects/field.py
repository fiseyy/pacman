from logic.field import Field
import pyray as pr

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
