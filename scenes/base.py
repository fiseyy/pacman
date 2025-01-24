from settings import font
import pyray as pr
# Базовый класс для сцен
class SceneBase:
    """
    Базовый класс для всех сцен.

    Методы:
        enter(): Входит в сцену.
        exit(): Выходит из сцены.
        update(): Обновляет сцену.
        draw(): Рисует сцену.
    """

    def enter(self):
        """
        Входит в сцену.
        """
        pass

    def exit(self):
        """
        Выходит из сцены.
        """
        pass

    def update(self):
        """
        Обновляет сцену.
        """
        pass

    def draw(self):
        """
        Рисует сцену.
        """
        pass
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
    text_width = pr.measure_text_ex(font, text, font_size, 1.0).x
    pr.draw_text_ex(font, text, (x + 10, y + 10), font_size, 1.0, pr.BLACK)