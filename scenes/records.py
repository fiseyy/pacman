import pyray as pr
from scenes.base import SceneBase, draw_button
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT, BUTTON_WIDTH, BUTTON_HEIGHT

class RecordsScene(SceneBase):
    def __init__(self, state):
        self.state = state
        self.is_exiting = False  # Флаг для отслеживания выхода

    def enter(self):
        print("Entering Records Scene")

    def draw(self):
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Records Scene", (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2), FONT_SIZE, 1.0, WHITE_TEXT)
        draw_button("Back to main menu", SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2 + 200, BUTTON_WIDTH+150, BUTTON_HEIGHT, FONT_SIZE, on_click=self.exit)

    def exit(self):
        if not self.is_exiting:  # Проверяем, не выходим ли мы уже
            self.is_exiting = True  # Устанавливаем флаг
            print("Exiting Records Scene")
            self.state.change_scene("menu")  # Переход в меню