from scenes.base import SceneBase
from scenes.game import GameScene
import pyray as pr
from settings import BLACK_BACKGROUND, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT,font, BUTTON_WIDTH, BUTTON_HEIGHT,RED_TEXT

# Функция для рисования кнопки
def draw_button(text: str, x: int, y: int, width: int, height: int, font_size: int, on_click=None, active_color=pr.DARKGRAY, inactive_color=pr.LIGHTGRAY) -> None:
    """
   Рисует кнопку на экране.

   Аргументы:
       text (str): Текст кнопки.
       x (int): Координата x кнопки.
       y (int): Координата y кнопки.
       width (int): Ширина кнопки.
       height (int): Высота кнопки.
       font_size (int): Размер шрифта текста кнопки.
       on_click (callable, optional): Функция, которая будет вызвана при нажатии на кнопку. По умолчанию None.
       active_color (tuple, optional): Цвет кнопки при наведении курсора. По умолчанию rl.DARK_GRAY.
       inactive_color (tuple, optional): Цвет кнопки при отсутствии наведения курсора. По умолчанию rl.LIGHT_GRAY.
   """
    button_color = inactive_color
    if pr.check_collision_point_rec(pr.get_mouse_position(), [x, y, width, height]):
        button_color = active_color
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT) and on_click:
            on_click()
    # Рисуем кнопку
    pr.draw_rectangle(x, y, width, height, button_color)
    pr.draw_text_ex(font, "PAC-MAN".encode(), (SCREEN_WIDTH // 2 - 150, 100), 100, 1.0, RED_TEXT)
    text_width = pr.measure_text_ex(font, text, font_size, 1.0).x
    pr.draw_text_ex(font, text, (x + (width - text_width) // 2, y + 10), font_size, 1.0, pr.BLACK)

class MenuScene(SceneBase):
    """
   Класс для сцены меню.

   Методы:
       enter(): Входит в сцену меню.
       draw(): Рисует сцену меню.
    """
    def __init__(self, state):
        self.state = state
        # super().__init__()
    def enter(self):
        """
       Входит в сцену меню.
        """
        print("Entering Menu Scene")

    def draw(self):
        """
       Рисует сцену меню.
        """
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "PAC-MAN", (SCREEN_WIDTH // 2 - 150, 100), 100, 1.0, RED_TEXT)
        draw_button("Play", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.state.change_scene(GameScene()))
        draw_button("Exit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, on_click=lambda: pr.close_window())