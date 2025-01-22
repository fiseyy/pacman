from scenes.base import SceneBase, draw_button
import pyray as pr
from settings import BLACK_BACKGROUND, font, SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE, WHITE_TEXT, BUTTON_HEIGHT, BUTTON_WIDTH
class SettingsScene(SceneBase):
    """
   Класс для сцены настроек.

   Методы:
       enter(): Входит в сцену настроек.
       draw(): Рисует сцену настроек.
    """
    def __init__(self, state):
        """
       Инициализирует сцену настроек.
       :param game: Объект класса Game.
        """
        self.state = state
        self.is_exiting = False  # Флаг для отслеживания выхода
    def enter(self):
        """
       Входит в сцену настроек.
        """
        print("Entering Settings Scene")

    def draw(self):
        """
       Рисует сцену настроек.
        """
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Settings Scene", (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)
        draw_button("Back to main menu", SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2 + 200, BUTTON_WIDTH+150, BUTTON_HEIGHT, FONT_SIZE, on_click=self.exit)
    def exit(self):
        """
       Выходит из сцены настроек.
        """
        if not self.is_exiting:  # Проверяем, не выходим ли мы уже
            self.is_exiting = True  # Устанавливаем флаг
            print("Exiting Settings Scene")
            self.state.change_scene("menu")  # Переход в меню