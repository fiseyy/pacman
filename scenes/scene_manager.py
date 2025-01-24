from scenes.menu import MenuScene
from scenes.base import SceneBase
from scenes.pause import PauseScene
from scenes.game import GameScene
from scenes.records import RecordsScene
from scenes.settings import SettingsScene
import pyray as pr
# scene_manager.py
class GameState:
    def __init__(self):
        self.current_scene = None  # Изначально нет текущей сцены
        self.change_scene("menu")  # Переход в меню

    def change_scene(self, new_scene: str):
        if self.current_scene:
            self.current_scene.exit()  # Выходим из текущей сцены

        # Отложенный импорт для избежания циклических зависимостей
        if new_scene == "menu":
            from scenes.menu import MenuScene
            self.current_scene = MenuScene(self)
        elif new_scene == "game":
            from scenes.game import GameScene
            self.current_scene = GameScene(18)
        elif new_scene == "pause":
            from scenes.pause import PauseScene
            self.current_scene = PauseScene()
        elif new_scene == "records":
            from scenes.records import RecordsScene
            self.current_scene = RecordsScene(self)
        elif new_scene == "settings":
            self.current_scene = SettingsScene(self)
        self.current_scene.enter()  # Входим в новую сцену

# Создаем объект состояния игры
state = GameState()
      
def handle_key_presses() -> None:
    """
    Обработка нажатий клавиш для управления сценами.
    """
    if pr.is_key_pressed(pr.KEY_P):
        if isinstance(state.current_scene, GameScene):
            state.change_scene("pause") # Переход в сцену паузы
        elif isinstance(state.current_scene, PauseScene):
            state.change_scene("game")  # Переход в меню
    if pr.is_key_pressed(pr.KEY_Q):
        if isinstance(state.current_scene, GameScene):
            state.change_scene("menu")
        if isinstance(state.current_scene, PauseScene):
            state.change_scene("menu")