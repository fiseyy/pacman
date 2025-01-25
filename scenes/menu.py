from scenes.base import draw_button, SceneBase
import pyray as pr
from settings import BLACK_BACKGROUND, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, font, BUTTON_WIDTH, BUTTON_HEIGHT, RED_TEXT, load_settings
class MenuScene(SceneBase):
    def __init__(self, state):
        self.state = state
        self.main_menu_music = None
        self.button_click_sound = None
        self.start_game_sound = None
        self.sound_stream = None
    def enter(self):
        print("Entering Menu Scene")
        pr.init_audio_device()
        self.main_menu_music = pr.load_music_stream("sounds/main_menu.mp3")
        self.button_click_sound = pr.load_sound("sounds/ui/button_clicked.mp3")
        self.start_game_sound = pr.load_sound("sounds/ui/start_game.mp3")
        if self.main_menu_music and self.start_game_sound and self.button_click_sound:
            print("Music and sound stream loaded successfully.")
            try:
                music_volume = load_settings()["MUSIC_VOLUME"]
                sound_volume = load_settings()["SOUND_VOLUME"]
                pr.set_music_volume(self.main_menu_music, music_volume)
                pr.set_sound_volume(self.button_click_sound, sound_volume)
                pr.set_sound_volume(self.start_game_sound, sound_volume)
                pr.play_music_stream(self.main_menu_music)  # Воспроизведение музыки
            except Exception as e:
                print(f"Error while setting music volume: {e}")
        else:
            print("Failed to load music and sound stream.")
    def start_game_clicked(self):
        pr.play_sound(self.start_game_sound)
        pr.wait_time(1)
        self.state.change_scene("game")
    def button_clicked(self, new_scene):
        pr.play_sound(self.button_click_sound)
        pr.wait_time(0.5)
        self.state.change_scene(new_scene)
    def draw(self):
        pr.clear_background(BLACK_BACKGROUND)
        pr.update_music_stream(self.main_menu_music)
        pr.draw_text_ex(font, "PAC-MAN", (SCREEN_WIDTH // 2 - 200, 100), 100, 1.0, RED_TEXT)
        draw_button("Play", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.start_game_clicked())
        draw_button("Records", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.button_clicked("records"))
        draw_button("Settings", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, lambda: self.button_clicked("settings"))
        draw_button("Exit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, BUTTON_WIDTH, BUTTON_HEIGHT, FONT_SIZE, on_click=lambda: pr.close_window())
    def exit(self):
        pr.stop_music_stream(self.main_menu_music)  # Остановка музыки при выходе
        pr.unload_music_stream(self.main_menu_music)  # Освобождение ресурсов
        pr.close_audio_device()