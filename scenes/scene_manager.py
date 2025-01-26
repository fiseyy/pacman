from scenes.menu import MenuScene
from scenes.base import SceneBase
from scenes.pause import PauseScene
from scenes.game import GameScene
from scenes.records import RecordsScene
from scenes.settings import SettingsScene
from scenes.game_over import GameOverScene
from settings import CELL_SIZE
import pyray as pr
# scene_manager.py
class GameState:
    def __init__(self):
        pr.init_audio_device()
        self.current_scene = None  # Изначально нет текущей сцены
        self.change_scene("menu")  # Переход в меню

    def change_scene(self, new_scene: str):
        if self.current_scene:
            self.current_scene.exit()  # Выходим из текущей сцены

        # Отложенный импорт для избежания циклических зависимостей
        if new_scene == "menu":
            self.current_scene = MenuScene(self)
        elif new_scene == "game":
            self.current_scene = GameScene(self,CELL_SIZE, None, None)
        elif new_scene == "pause":
            self.current_scene = PauseScene()
        elif new_scene == "records":
            self.current_scene = RecordsScene(self)
        elif new_scene == "settings":
            self.current_scene = SettingsScene(self)
        self.current_scene.enter()  # Входим в новую сцену
    def restart_game(self, lifes_counter = None, score_counter = None):
        self.current_scene.exit()
        self.current_scene = GameScene(self,CELL_SIZE, lifes_counter, score_counter)
    def game_over(self,score):
        self.current_scene.exit()
        self.current_scene = GameOverScene(self)
        self.current_scene.enter(score)
    def pause_game(self):
        if isinstance(self.current_scene, GameScene):
            self.saved_pacman = self.current_scene.pacman
            self.saved_ghosts = [self.current_scene.blinky_ghost,
                                 self.current_scene.clyde_ghost,
                                 self.current_scene.pinky_ghost,
                                 self.current_scene.inky_ghost]
            self.life_counter = self.current_scene.life_counter
            self.score_counter = self.current_scene.score_counter
            self.field_drawer = self.current_scene.field_drawer
            self.change_scene("pause") # Переход в сцену паузы
        elif isinstance(state.current_scene, PauseScene):
            self.current_scene.exit()
            self.current_scene = GameScene(self,CELL_SIZE, self.life_counter, self.score_counter)
            self.current_scene.pacman = self.saved_pacman
            self.current_scene.pacman.unpause()
            self.current_scene.field_drawer = self.field_drawer
            self.current_scene.blinky_ghost = self.saved_ghosts[0]
            self.current_scene.clyde_ghost = self.saved_ghosts[1]
            self.current_scene.pinky_ghost = self.saved_ghosts[2]
            self.current_scene.inky_ghost = self.saved_ghosts[3]

# Создаем объект состояния игры
state = GameState()
      
def handle_key_presses() -> None:
    """
    Обработка нажатий клавиш для управления сценами.
    """
    if pr.is_key_pressed(pr.KEY_P):
        state.pause_game()
    if pr.is_key_pressed(pr.KEY_Q):
        if isinstance(state.current_scene, GameScene):
            state.change_scene("menu")
        if isinstance(state.current_scene, PauseScene):
            state.change_scene("menu")