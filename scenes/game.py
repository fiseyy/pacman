import pyray as pr
from scenes.base import SceneBase
from objects.cherry import Cherry
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT
from objects.field import FieldDrawer, Textures
from logic.field import Field
from objects.ghosts.inky import InkyGhost
class GameScene(SceneBase):
    """
   Класс для игровой сцены.

   Методы:
       enter(): Входит в игровую сцену.
       draw(): Рисует игровую сцену.
    """
    def __init__(self,cell_size):
        self.x_to_center = 0
        self.y_to_center = 0
        self.field = Field("objects/maps/field.txt")
        self.field_drawer = FieldDrawer(self.field,cell_size)
        self.inky_ghost = InkyGhost(x=1, y=1,cell_size=cell_size, field=self.field)
        super().__init__()
    def enter(self):
        """
       Входит в игровую сцену.
        """
        self.cherry=Cherry(100,100,20)
        self.cherry.show()
        print("Entering Game Scene")

    def draw(self):
        """
       Рисует игровую сцену.
        """
        
        pr.clear_background(BLACK_BACKGROUND)
        #pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, 5), FONT_SIZE, 1.0, WHITE_TEXT)
        self.field_drawer.draw(self.x_to_center, self.y_to_center)
        self.process_additional_logic()  # Обработка дополнительной логики
        self.inky_ghost.update()  # Обновляем состояние Inky
        self.inky_ghost.draw()    # Рисуем Inky
    def process_additional_logic(self):
        self.inky_ghost.change_direction(self.field)
        self.cherry.logic()
