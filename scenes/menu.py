from scenes.base import draw_button, SceneBase
import pyray as pr
from settings import BLACK_BACKGROUND, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, font, BUTTON_WIDTH, BUTTON_HEIGHT, RED_TEXT

class MenuScene(SceneBase):
    def __init__(self, state):
        self.state = state

    def enter(self):
        print("Entering Menu Scene")

    def draw(self):
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "PAC-MAN", (SCREEN_WIDTH // 2 - 200, 100), 100, 1.0, RED_TEXT)
        draw_button("Play", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.state.change_scene("game"))
        draw_button("Records", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.state.change_scene("records"))
        draw_button("Settings", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.state.change_scene("settings"))
        draw_button("Exit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, on_click=lambda: pr.close_window())