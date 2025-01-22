from logic.field import Field
import pyray as pr

# Класс для преобразования изображений в текстуры
class Textures:
   """
   Класс для работы с текстурами.

   Атрибуты:
       seed (pr.Texture): Текстура малого зерна.
       energizer (pr.Texture): Текстура большого зерна.
       textures (dict): Словарь текстур.

   Методы:
       get_texture(texture_name): Возвращает текстуру по имени.
       unload(): Выгружает текстуры.
   """

   def __init__(self):
       """
       Инициализирует объект класса Textures.
       """
       self.seed = pr.load_texture_from_image(pr.load_image("images/corn_1.png"))  # текстура малого зерна
       self.energizer = pr.load_texture_from_image(pr.load_image("images/corn_2.png"))  # текстура большого зерна
       self.textures = {
           "seed": self.seed,
           "energizer": self.energizer
       }

   def get_texture(self, texture_name):
       """
       Возвращает текстуру по имени.

       Аргументы:
           texture_name (str): Имя текстуры.

       Возвращает:
           pr.Texture: Текстура.
       """
       return self.textures[texture_name]

   def unload(self):
       """
       Выгружает текстуры.
       """
       pr.unload_texture(self.seed)
       pr.unload_texture(self.energizer)

class FieldDrawer:
   """
   Класс для отрисовки поля.

   Атрибуты:
       field (Field): Поле для отрисовки.
       cell_size (int): Размер ячейки.
       textures (Textures): Объект класса Textures для работы с текстурами.

   Методы:
       draw(): Рисует поле.
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

   def draw(self):
       """
       Рисует поле.
       """
       for y, row in enumerate(self.field):
           for x, cell in enumerate(row):
               if cell == '#':
                   pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.BLUE)  # Стены
               elif cell == '_':
                   pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.BLACK)  # Пустые ячейки
               elif cell == '.':
                   # малое зерно
                   texture = self.textures.get_texture("seed")
                   pr.draw_texture(texture, x * self.cell_size, y * self.cell_size, pr.WHITE)
                   # pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW) # старая реализация малого зерна
               elif cell == 'S':
                   # большое зерно
                   texture = self.textures.get_texture("energizer")
                   pr.draw_texture(texture, x * self.cell_size, y * self.cell_size, pr.WHITE)
                   # pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW) # старая реализация большого зерна
               elif cell == 'T':
                   pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)
