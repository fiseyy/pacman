import pyray as pr
from scenes.base import SceneBase
from objects.cherry import Cherry
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT
class GameScene(SceneBase):
    """
   Класс для игровой сцены.

   Методы:
       enter(): Входит в игровую сцену.
       draw(): Рисует игровую сцену.
    """
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
        self.cherry.logic()
        pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)