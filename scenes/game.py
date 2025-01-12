import pyray as pr
from scenes.base import SceneBase
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
        print("Entering Game Scene")

    def draw(self):
        """
       Рисует игровую сцену.
        """
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)