from scenes.menu import MenuScene
from scenes.base import SceneBase
from scenes.pause import PauseScene
from scenes.game import GameScene
import pyray as pr
class GameState:
    """
   Класс для управления состоянием игры.

   Атрибуты:
       current_scene (SceneBase): Текущая сцена игры.

   Методы:
       change_scene(new_scene): Меняет текущую сцену на новую.
   """
    def __init__(self):
        """
       Инициализирует объект класса GameState.

       Атрибуты:
           current_scene (SceneBase): Начальная сцена игры.
       """
        self.current_scene = MenuScene(self)  # Начинаем с меню
        self.current_scene.enter()  # Входим в начальную сцену

    def change_scene(self, new_scene: SceneBase):
        """
       Меняет текущую сцену на новую.

       Аргументы:
           new_scene (SceneBase): Новая сцена игры.
       """
        self.current_scene.exit()  # Выходим из текущей сцены
        self.current_scene = new_scene  # Меняем сцену
        self.current_scene.enter()  # Входим в новую сцену

# Создаем объект состояния игры
state = GameState()

def handle_key_presses() -> None:
    """
    Обработка нажатий клавиш для управления сценами.
    """
    if pr.is_key_pressed(pr.KEY_P):
        if isinstance(state.current_scene, GameScene):
            state.change_scene(PauseScene())  # Переход в сцену паузы
        elif isinstance(state.current_scene, PauseScene):
            state.change_scene(MenuScene(state))  # Переход в меню
