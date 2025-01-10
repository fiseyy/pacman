from base import SceneBase
import raylib as rl
from settings import BLACK_BACKGROUND, font, SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE, WHITE_TEXT
class SettingsScene(SceneBase):
    """
   Класс для сцены настроек.

   Методы:
       enter(): Входит в сцену настроек.
       draw(): Рисует сцену настроек.
    """
    def enter(self):
        """
       Входит в сцену настроек.
        """
        print("Entering Settings Scene")

    def draw(self):
        """
       Рисует сцену настроек.
        """
        rl.ClearBackground(BLACK_BACKGROUND)
        rl.DrawTextEx(font, "Settings Scene".encode(), (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)