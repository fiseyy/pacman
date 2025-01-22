import pyray as pr
from scenes.base import SceneBase
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT
from objects.field import FieldDrawer, Textures
from logic.field import Field
class GameScene(SceneBase):
    """
   Класс для игровой сцены.

   Методы:
       enter(): Входит в игровую сцену.
       draw(): Рисует игровую сцену.
    """
    def __init__(self):
        self.field = Field("objects/maps/field.txt")
        self.field_drawer = FieldDrawer(self.field,15)
        super().__init__()
    def enter(self):
        """
       Входит в игровую сцену.
        """
        print("Entering Game Scene")

    def draw(self):
        """
       Рисует игровую сцену.
        """
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, 5), FONT_SIZE, 1.0, WHITE_TEXT)
        x_to_center = 200
        y_to_center = 50
        self.field_drawer.draw(x_to_center, y_to_center)
