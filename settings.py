from raylib import LoadFont, GetFontDefault
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
try:
    font = LoadFont("ofont.ru_Zeitmax.ttf".encode())  # Путь к шрифту
except Exception as e:
    print(f"Ошибка загрузки шрифта: {e}")
    font = GetFontDefault()  # Используем стандартный шрифт, если пользовательский не загрузился