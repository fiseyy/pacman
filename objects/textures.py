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
                "right": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_right_1.png")),
                "up_alt": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_up_2.png")),
                "down_alt": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_down_2.png")),
                "left_alt": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_left_2.png")),
                "right_alt": pr.load_texture_from_image(pr.load_image("images/pacman/pacman_right_2.png")),
                "death_1": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_1.png")),
                "death_2": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_2.png")),
                "death_3": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_3.png")),
                "death_4": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_4.png")),
                "death_5": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_5.png")),
                "death_6": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_6.png")),
                "death_7": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_7.png")),
                "death_8": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_8.png")),
                "death_9": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_9.png")),
                "death_10": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_10.png")),
                "death_11": pr.load_texture_from_image(pr.load_image("images/pacman/death/pacman_death_11.png")),
            },
            "life": pr.load_texture_from_image(pr.load_image("images/heart.png"))
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