import pyray as pr
# Класс для преобразования изображений в текстуры
class Textures:
   """
   Класс для работы с текстурами.

   Атрибуты:
       seed (pr.Texture): Текстура малого зерна.
       energizer (pr.Texture): Текстура большого зерна.
       textures (dict): Словарь текстур.

   Методы:
       get_texture(texture_name): Возвращает текстуру по имени.
       unload(): Выгружает текстуры.
   """

   def __init__(self):
       """
       Инициализирует объект класса Textures.
       """
       self.seed = pr.load_texture_from_image(pr.load_image("images/corn_1.png"))  # текстура малого зерна
       self.energizer = pr.load_texture_from_image(pr.load_image("images/corn_2.png"))  # текстура большого зерна
       self.textures = {
           "seed": self.seed,
           "energizer": self.energizer,
           "blinky": {
               "up": pr.load_texture_from_image(pr.load_image("images/ghosts/blinky/blinky_up_1.png")),
               "down": pr.load_texture_from_image(pr.load_image("images/ghosts/blinky/blinky_down_1.png")),
               "left": pr.load_texture_from_image(pr.load_image("images/ghosts/blinky/blinky_left_1.png")),
               "right": pr.load_texture_from_image(pr.load_image("images/ghosts/blinky/blinky_right_1.png"))
            },
           "clyde": {
               "up": pr.load_texture_from_image(pr.load_image("images/ghosts/clyde/clyde_up_1.png")),
               "down": pr.load_texture_from_image(pr.load_image("images/ghosts/clyde/clyde_down_1.png")),
               "left": pr.load_texture_from_image(pr.load_image("images/ghosts/clyde/clyde_left_1.png")),
               "right": pr.load_texture_from_image(pr.load_image("images/ghosts/clyde/clyde_right_1.png"))
            },
           "inky": {
               "up": pr.load_texture_from_image(pr.load_image("images/ghosts/inky/inky_up_1.png")),
               "down": pr.load_texture_from_image(pr.load_image("images/ghosts/inky/inky_down_1.png")),
               "left": pr.load_texture_from_image(pr.load_image("images/ghosts/inky/inky_left_1.png")),
               "right": pr.load_texture_from_image(pr.load_image("images/ghosts/inky/inky_right_1.png"))
            },
           "pinky": {
               "up": pr.load_texture_from_image(pr.load_image("images/ghosts/pinky/pinky_up_1.png")),
               "down": pr.load_texture_from_image(pr.load_image("images/ghosts/pinky/pinky_down_1.png")),
               "left": pr.load_texture_from_image(pr.load_image("images/ghosts/pinky/pinky_left_1.png")),
               "right": pr.load_texture_from_image(pr.load_image("images/ghosts/pinky/pinky_right_1.png"))
            },
            "pacman": {
                "up": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_up_1.png")),
                "down": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_down_1.png")),
                "left": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_left_1.png")),
                "right": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_right_1.png"))
            }
       }

   def get_texture(self, texture_name):
       """
       Возвращает текстуру по имени.

       Аргументы:
           texture_name (str): Имя текстуры.

       Возвращает:
           pr.Texture: Текстура.
       """
       return self.textures[texture_name]

   def unload(self):
       """
       Выгружает текстуры.
       """
       pr.unload_texture(self.seed)
       pr.unload_texture(self.energizer)