from scenes.base import SceneBase
from settings import BLACK_BACKGROUND, WHITE_TEXT, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, font
import raylib as rl
class PauseScene(SceneBase):
    """
    Класс для сцены паузы.

    Методы:
        enter(): Входит в сцену паузы.
        draw(): Рисует сцену паузы.
    """
    def enter(self):
        """
       Входит в сцену паузы.
        """
        print("Entering Pause Scene")

    def draw(self):
        """
       Рисует сцену паузы.
        """
        rl.ClearBackground(BLACK_BACKGROUND)
        rl.DrawTextEx(font, "Pause Scene".encode(), (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)