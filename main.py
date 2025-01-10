import raylib as rl
from settings import *
from scenes.scene_manager import handle_key_presses, state
rl.InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "PAC-MAN Game".encode())  # Инициализация окна
rl.SetTargetFPS(60)  # Установка целевого FPS

# Основной цикл игры
while not rl.WindowShouldClose():
    rl.BeginDrawing()
    handle_key_presses()
    state.current_scene.draw()
    rl.EndDrawing()
rl.CloseWindow()
