from scenes.base import SceneBase, draw_button
import pyray as pr
from settings import BLACK_BACKGROUND, font, SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE, WHITE_TEXT, BUTTON_HEIGHT, BUTTON_WIDTH, sound
MUSIC_VOLUME = sound["MUSIC_VOLUME"]
SOUND_VOLUME = sound["SOUND_VOLUME"]
class MusicChangerButton():
    def __init__(self):
        self.music_volume = MUSIC_VOLUME
        self.changed = False
        self.params = {
            "input_text": str(MUSIC_VOLUME),
            "font_size": 20,
            "input_box": [100, 100, 600, 30], # x,y,width,height
            "active": False
        }

    def draw(self):
        if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
            if pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(*self.params["input_box"])):
                self.params["active"] = not self.params["active"]
            else:
                self.params["active"] = False

        if self.params["active"]:
            # Получение символов, введенных с клавиатуры
            key = pr.get_key_pressed()
            while key > 0:
                if key == pr.KeyboardKey.KEY_BACKSPACE:  # Код клавиши Backspace
                    self.params["input_text"] = str(self.params["input_text"])[:-1]  # Удаляем последний символ
                else:
                    self.params["input_text"] += chr(key)  # Добавляем символ
                key = pr.get_key_pressed()

            # Ограничение длины текста
            if len(self.params["input_text"]) > 20:
                self.params["input_text"] = self.params["input_text"][:20]
            self.save_if_changed()
        pr.draw_rectangle_rec(pr.Rectangle(*self.params["input_box"]), pr.LIGHTGRAY)
        pr.draw_rectangle_lines(self.params["input_box"][0], self.params["input_box"][1], self.params["input_box"][2], self.params["input_box"][3], pr.DARKGRAY)
        # Рисуем текст
        pr.draw_text(self.params["input_text"], self.params["input_box"][0] + 5, self.params["input_box"][1] + 5, self.params["font_size"], pr.DARKGRAY)
        pr.draw_text("Music volume", 100, 50, FONT_SIZE, pr.WHITE)
    def save_if_changed(self):
        # Сохраняем значение, если оно изменилось
        if self.params["input_text"] != str(self.music_volume):
            try:
                self.music_volume = float(self.params["input_text"])
                if self.music_volume >= 0.0 and self.music_volume <= 1.0:
                    self.changed = True
            except ValueError:
                return False
            
    def changed(self):
        if self.music_volume == MUSIC_VOLUME:
            return False
        return True

class SoundChangerButton():
    def __init__(self):
        self.sound_volume = SOUND_VOLUME
        self.changed = False
        self.params = {
            "input_text": str(SOUND_VOLUME),
            "font_size": 20,
            "input_box": [100, 200, 600, 30], # x,y,width,height
            "active": False
        }

    def draw(self):
        if pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
            if pr.check_collision_point_rec(pr.get_mouse_position(), pr.Rectangle(*self.params["input_box"])):
                self.params["active"] = not self.params["active"]
            else:
                self.params["active"] = False

        if self.params["active"]:
            # Получение символов, введенных с клавиатуры
            key = pr.get_key_pressed()
            while key > 0:
                if key == pr.KeyboardKey.KEY_BACKSPACE:  # Код клавиши Backspace
                    self.params["input_text"] = str(self.params["input_text"])[:-1]  # Удаляем последний символ
                else:
                    self.params["input_text"] += chr(key)  # Добавляем символ
                key = pr.get_key_pressed()

            # Ограничение длины текста
            if len(self.params["input_text"]) > 20:
                self.params["input_text"] = self.params["input_text"][:20]
            self.save_if_changed()
        pr.draw_rectangle_rec(pr.Rectangle(*self.params["input_box"]), pr.LIGHTGRAY)
        pr.draw_rectangle_lines(self.params["input_box"][0], self.params["input_box"][1], self.params["input_box"][2], self.params["input_box"][3], pr.DARKGRAY)
        # Рисуем текст
        pr.draw_text(self.params["input_text"], self.params["input_box"][0] + 5, self.params["input_box"][1] + 5, self.params["font_size"], pr.DARKGRAY)
        pr.draw_text("Sound volume", 100, 150, FONT_SIZE, pr.WHITE)
    def save_if_changed(self):
        # Сохраняем значение, если оно изменилось
        if self.params["input_text"] != str(self.sound_volume):
            try:
                self.sound_volume = float(self.params["input_text"])
                if self.sound_volume >= 0.0 and self.sound_volume <= 1.0:
                    self.changed = True
            except ValueError:
                return False
            

            
class SettingsScene(SceneBase):
    """
   Класс для сцены настроек.

   Методы:
       enter(): Входит в сцену настроек.
       draw(): Рисует сцену настроек.
    """
    def __init__(self, state):
        """
       Инициализирует сцену настроек.
       :param game: Объект класса Game.
        """
        self.music_changer = MusicChangerButton()
        self.sound_changer = SoundChangerButton()
        self.state = state
        self.is_exiting = False  # Флаг для отслеживания выхода
    def enter(self):
        """
       Входит в сцену настроек.
        """
        print("Entering Settings Scene")
        # Переменные для текстового поля
        
    def apply_changes(self):
        print("apply")
        if self.music_changer.changed:
            MUSIC_VOLUME = self.music_changer.music_volume
        if self.sound_changer.changed:
            SOUND_VOLUME = self.sound_changer.sound_volume
        self.music_changer.changed = False
        self.sound_changer.changed = False
        
    def discard_changes(self):
        print("discard")
        self.music_changer.params["input_text"] = str(MUSIC_VOLUME)
        self.sound_changer.params["input_text"] = str(SOUND_VOLUME)
        self.music_changer.changed = False
        self.sound_changer.changed = False
    def draw(self):
        """
       Рисует сцену настроек.
        """
        self.music_changer.draw()
        self.sound_changer.draw()
        pr.clear_background(BLACK_BACKGROUND)
        pr.draw_text_ex(font, "Settings Scene", (SCREEN_WIDTH // 2 - 120, 5), FONT_SIZE, 1.0, WHITE_TEXT)
        if self.music_changer.changed or self.sound_changer.changed:
            draw_button("Apply Changes", SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2+80,BUTTON_WIDTH+150, BUTTON_HEIGHT, FONT_SIZE, on_click=self.apply_changes)
            draw_button("Discard Changes", SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2 + 140,BUTTON_WIDTH+150, BUTTON_HEIGHT, FONT_SIZE, on_click=self.discard_changes)
        draw_button("Back to main menu", SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2 + 200, BUTTON_WIDTH+150, BUTTON_HEIGHT, FONT_SIZE, on_click=self.exit)
    def exit(self):
        """
       Выходит из сцены настроек.
        """
        if not self.is_exiting:  # Проверяем, не выходим ли мы уже
            self.is_exiting = True  # Устанавливаем флаг
            print("Exiting Settings Scene")
            self.state.change_scene("menu")  # Переход в меню