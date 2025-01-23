from pyray import get_font_default
import json
SCREEN_WIDTH = 800  # Ширина окна
SCREEN_HEIGHT = 600  # Высота окна
YELLOW_BACKGROUND = (255, 255, 0, 255)  # Желтый фон
BLACK_BACKGROUND = (0, 0, 0, 255)  # Черный фон
WHITE_TEXT = (255, 255, 255, 255)  # Белый текст
RED_TEXT = (255, 0, 0, 255)  # Красный текст
FONT_SIZE = 40  # Размер шрифта
BUTTON_WIDTH = 200  # Ширина кнопки
BUTTON_HEIGHT = 50  # Высота кнопки
# Загрузка шрифта
font = get_font_default()


# Загрузка настроек из файла
def load_settings(filename='settings.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "MUSIC_VOLUME": 0.5,
            "SOUND_VOLUME": 0.5
        }

# Сохранение настроек в файл
def save_settings(settings, filename='settings.json'):
    with open(filename, 'w') as f:
        json.dump(settings, f)
    
# Загрузка начальных настроек
sound = load_settings()