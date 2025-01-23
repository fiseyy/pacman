from logic.field import Field
import pyray as pr
from objects.textures import Textures

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

   def draw(self,x_to_center=0, y_to_center=0):
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
               elif cell == '.':
                   # малое зерно
                   texture = self.textures.get_texture("seed")
                   pr.draw_texture(texture, x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, pr.WHITE)
                   # pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW) # старая реализация малого зерна
               elif cell == 'S':
                   # большое зерно
                   texture = self.textures.get_texture("energizer")
                   pr.draw_texture(texture, x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, pr.WHITE)
                   # pr.draw_rectangle(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW) # старая реализация большого зерна
               elif cell == 'T':
                   pr.draw_rectangle(x_to_center + x * self.cell_size, y_to_center + y * self.cell_size, self.cell_size, self.cell_size, pr.YELLOW)
