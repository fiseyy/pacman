from scenes.base import SceneBase, draw_button
from settings import BLACK_BACKGROUND, WHITE_TEXT, RED_TEXT, FONT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, font, BUTTON_WIDTH, BUTTON_HEIGHT, load_settings
import pyray as pr
from logic.records import Records, Record
class GameOverScene(SceneBase):
    """
    Класс для сцены паузы.

    Методы:
        enter(): Входит в сцену паузы.
        draw(): Рисует сцену паузы.
    """
    def __init__(self,state):
        self.state = state
        self.button_click_sound = pr.load_sound("sounds/ui/button_clicked.mp3")
        try:
                music_volume = load_settings()["MUSIC_VOLUME"]
                sound_volume = load_settings()["SOUND_VOLUME"]
                pr.set_sound_volume(self.button_click_sound, sound_volume)
        except Exception as e:
                print(f"Error while setting music volume: {e}")
    def enter(self, score):
        """
       Входит в сцену паузы.
        """
        self.score = score
        record = Record(self.score)
        records = Records()
        records.load_records()
        records.add_record(record)
        records.save_records()
        
        print("Entering Game Over Scene")

    def button_clicked(self, new_scene):
        pr.play_sound(self.button_click_sound)
        pr.wait_time(0.5)
        self.state.change_scene(new_scene)
    def draw(self):
        """
       Рисует сцену паузы.
        """
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Game over!", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 200), FONT_SIZE, 1.0, RED_TEXT)
        pr.draw_text_ex(font, f"Your Score: {self.score}", (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50), FONT_SIZE, 1.0, WHITE_TEXT)
        draw_button("Back to main menu", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 200, BUTTON_WIDTH + 140, BUTTON_HEIGHT, FONT_SIZE, lambda: self.button_clicked("menu"))
    def exit(self):
        pr.unload_sound(self.button_click_sound)