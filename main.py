import pyray as pr
from settings import *
from scenes.scene_manager import handle_key_presses, state
pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "PAC-MAN Game")  # Инициализация окна
pr.set_target_fps(60)  # Установка целевого FPS

# Основной цикл игры
while not pr.window_should_close():
    handle_key_presses()
    pr.begin_drawing()
    state.current_scene.draw()
    pr.end_drawing()
pr.close_window()
