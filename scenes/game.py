import raylib as rl
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
        rl.ClearBackground(BLACK_BACKGROUND)
        rl.DrawTextEx(font, "Game Scene".encode(), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)