import pyray as pr
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, load_settings

class Pacman():
   """
   Класс для управления пакманом.

   Атрибуты:
       speed (int): Скорость пакмана.
       pos_x (int): Абсолютное положение по горизонтали.
       pos_y (int): Абсолютное положение по вертикали.
       __cell_size (int): Сторона клетки (клетка - квадрат).
       pos_cell_x (int): Номер клетки по горизонтали.
       pos_cell_y (int): Номер клетки по вертикали.
       textures (Textures): Объект класса Textures для работы с текстурами.
       field (Field): Поле для проверки столкновений.
       texture (pr.Texture): Текстура пакмана.
       movement (PacmanMovement): Объект класса PacmanMovement для управления движением пакмана.
       changed_direction_on_crossroad (bool): Флаг, указывающий, изменилось ли направление на перекрестке.
       teleported_to_portal (bool): Флаг, указывающий, телепортировался ли пакман на портал.
       future_direction (tuple): Переменная для хранения будущего направления.

   Методы:
       draw(): Рисует пакмана.
       move(): Передвигает пакмана в 4х направлениях.
       goto(target_cell_pos): Перемещает пакмана на целевую позицию.
       define_direction(): Определяет направление движения клавишами WASD.
       can_turn(new_direction): Проверяет, может ли пакман повернуть в новое направление.
   """

   def __init__(self, x, y, cell_size, textures, field):
       """
       Инициализирует объект класса Pacman.

       Аргументы:
           x (int): Начальная позиция по горизонтали.
           y (int): Начальная позиция по вертикали.
           cell_size (int): Сторона клетки.
           textures (Textures): Объект класса Textures для работы с текстурами.
           field (Field): Поле для проверки столкновений.
       """
        # подключение звуков
       self.eating_corn_sound = pr.load_sound("sounds/game/eating_corn.mp3")
       self.turn_to_blue_sound = pr.load_sound("sounds/game/turn_to_blue.mp3")

       
       self.settings = load_settings()
       self.sound_volume = self.settings["SOUND_VOLUME"]

       pr.set_sound_volume(self.eating_corn_sound, self.sound_volume)
       pr.set_sound_volume(self.turn_to_blue_sound, self.sound_volume)


       self.speed = 1  # скорость пакмана
       self.pos_x = x * cell_size  # абсолютное положение по горизонтали
       self.pos_y = y * cell_size  # абсолютное положение по вертикали
       self.__cell_size = cell_size  # сторона клетки (клетка - квадрат)
       self.pos_cell_x = x  # номер клетки
       self.pos_cell_y = y  # номер клетки
       self.textures = textures
       self.field = field
       self.texture = self.textures["right"]
       self.movement = PacmanMovement(self.pos_cell_x, self.pos_cell_y, (1, 0), self.field)
       self.changed_direction_on_crossroad = False
       self.teleported_to_portal = False
       self.future_direction = None  # Переменная для хранения будущего направления
       self.animation_time = 0  # Время анимации
       self.animation_frame = 0  # Текущий кадр анимации
       self.animation_duration = 0.3  # Длительность одного кадра анимации (в секундах)
       self.collision = PacmanCollision(self.pos_cell_x, self.pos_cell_y, self.field, self)
       self.is_dead = False
       self.turn_to_blue = False
       self.turn_to_blue_start = None
       self.turn_to_blue_end = None

   def draw(self):
       """
       Рисует пакмана.
       """
       pr.draw_texture(self.texture, self.pos_x, self.pos_y, pr.WHITE)

   def texture_animation(self, pacman_direction):
       """Замена текстурок пакмана, при движении анимация

       Аргументы:
           pacman_direction (tuple): направление движения
       """
       if not self.is_dead:
        current_time = pr.get_time()  # Получаем текущее время в секундах
        frame = int(current_time / self.animation_duration) % 2
        if pacman_direction == (0, -1):  # Движение вверх
            if frame == 0:
                self.texture = self.textures["up"]
            else:
                if self.movement.can_move():
                    self.texture = self.textures["up_alt"]
        elif pacman_direction == (0, 1):  # Движение вниз
            if frame == 0:
                self.texture = self.textures["down"]
            else:
                if self.movement.can_move():
                    self.texture = self.textures["down_alt"]
        elif pacman_direction == (-1, 0):  # Движение влево
            if frame == 0:
                self.texture = self.textures["left"]
            else:
                if self.movement.can_move():
                    self.texture = self.textures["left_alt"]
        elif pacman_direction == (1, 0):  # Движение вправо
            if frame == 0:
                self.texture = self.textures["right"]
            else:
                if self.movement.can_move():
                    self.texture = self.textures["right_alt"]
   def death_animation(self):
        """Анимация смерти пакмана"""
        if not self.is_dead:
            self.is_dead = True
            self.death_start_time = pr.get_time()  # Сохраняем время начала анимации

        if self.is_dead:
            self.death_duration = 0.2
            self.max_death_frames = 10
            current_time = pr.get_time()  # Получаем текущее время в секундах
            elapsed_time = current_time - self.death_start_time  # Время, прошедшее с начала анимации
            frame = int(elapsed_time / self.death_duration)  # Определяем текущий кадр
            if frame < self.max_death_frames:
                self.texture = self.textures[f"death_{frame+1}"]  # Устанавливаем текстуру
            else:
                # Завершаем анимацию, устанавливаем финальную текстуру
                self.texture = self.textures["death_11"]  # Установите финальную текстуру
                #
   def death_animation_drawer(self):
    """Отрисовка анимации смерти пакмана"""
    if self.is_dead and not self.texture == self.textures["death_11"]:
        current_time = pr.get_time()  # Получаем текущее время в секундах
        elapsed_time = current_time - self.death_start_time  # Время, прошедшее с начала анимации
        frame = int(elapsed_time / self.death_duration)  # Определяем текущий кадр

        if frame < self.max_death_frames:
            self.texture = self.textures[f"death_{frame + 1}"]  # Устанавливаем текстуру
        else:
            self.texture = self.textures["death_11"]  # Устанавливаем финальную текстуру
            

        # Отрисовка Пакмана с текущей текстурой
        pr.draw_texture(self.texture, self.pos_x, self.pos_y, pr.WHITE)
   def move(self):
       """
       Передвигает пакмана в 4х направлениях.
       """
       # print(f"future {self.future_direction}, direction {self.movement.direction}") # DEBUG
       if not self.is_dead:
        if self.future_direction:
            if self.movement.can_move(self.future_direction) and self.pos_x % self.__cell_size == 0 and self.pos_y % self.__cell_size == 0 and not self.future_direction == self.movement.reverse_direction(self.movement.direction):
                self.movement.set_direction(self.future_direction)
            elif self.future_direction == self.movement.reverse_direction(self.movement.direction):
                self.movement.set_direction(self.future_direction)
        self.texture_animation(self.movement.direction)
        if self.movement.can_move():
            self.pos_x += self.movement.get_direction()[0] * self.speed
            self.pos_y += self.movement.get_direction()[1] * self.speed

            if self.pos_x / self.__cell_size % 1 == 0 and self.pos_y / self.__cell_size % 1 == 0:
                self.pos_cell_x = int(self.pos_x / self.__cell_size)
                self.pos_cell_y = int(self.pos_y / self.__cell_size)
                self.movement.pos_cell_x = self.pos_cell_x
                self.movement.pos_cell_y = self.pos_cell_y

        if self.movement.is_portal():
            if not self.teleported_to_portal:
                portal_positions = self.movement.get_portal_positions()
                portal_positions.remove((self.pos_cell_x, self.pos_cell_y))  # Удаляем текущую позицию
                if portal_positions:  # Проверяем, есть ли доступные порталы
                    self.goto(portal_positions[0])  # Перемещаемся на первый доступный портал
                    self.teleported_to_portal = True
        else:
            self.teleported_to_portal = False  # Сбрасываем флаг, если не на портале

   def goto(self, target_cell_pos: tuple):
       """
       Перемещает пакмана на целевую позицию.

       Аргументы:
           target_cell_pos (tuple): Целевая позиция.
       """
       if not self.is_dead:
        target_cell_x, target_cell_y = target_cell_pos
        self.pos_cell_x = target_cell_x
        self.pos_cell_y = target_cell_y
        self.pos_x = self.pos_cell_x * self.__cell_size
        self.pos_y = self.pos_cell_y * self.__cell_size
        self.movement.pos_cell_x = self.pos_cell_x
        self.movement.pos_cell_y = self.pos_cell_y

   def define_direction(self):
       """
       Определяет направление движения клавишами WASD.
       """
       if not self.is_dead:
        current_direction = self.movement.get_direction()

        if pr.is_key_down(pr.KeyboardKey.KEY_W) or pr.is_key_pressed(pr.KeyboardKey.KEY_W):  # Движение вверх
            self.future_direction = (0, -1)

        elif pr.is_key_down(pr.KeyboardKey.KEY_S) or pr.is_key_pressed(pr.KeyboardKey.KEY_S):  # Движение вниз
            self.future_direction = (0, 1)

        elif pr.is_key_down(pr.KeyboardKey.KEY_A) or pr.is_key_pressed(pr.KeyboardKey.KEY_A):  # Движение влево
            self.future_direction = (-1, 0)

        elif pr.is_key_down(pr.KeyboardKey.KEY_D) or pr.is_key_pressed(pr.KeyboardKey.KEY_D):  # Движение вправо
            self.future_direction = (1, 0)

   def can_turn(self, new_direction):
       """
       Проверяет, может ли пакман повернуть в новое направление.

       Аргументы:
           new_direction (tuple): Новое направление.

       Возвращает:
           bool: True, если пакман может повернуть в новое направление, иначе False.
       """
       if not self.is_dead:
        new_pos_x = self.pos_cell_x + new_direction[0]
        new_pos_y = self.pos_cell_y + new_direction[1]

        if new_pos_x < 0 or new_pos_x >= len(self.field.to_array()[0]) or new_pos_y < 0 or new_pos_y >= len(self.field.to_array()):
            return False  # Если новая позиция выходит за границы, поворот невозможен

        if self.field.to_array()[new_pos_y][new_pos_x] == "#":
            return False  # Если есть коллизия, поворот невозможен

        return True

class PacmanMovement:
   """
   Класс для управления движением пакмана.

   Атрибуты:
       pos_cell_x (int): Позиция пакмана по горизонтали.
       pos_cell_y (int): Позиция пакмана по вертикали.
       field (Field): Поле для проверки столкновений.
       direction (tuple): Направление движения пакмана.

   Методы:
       set_direction(direction): Устанавливает новое направление движения.
       get_direction(): Возвращает текущее направление движения.
       can_move(direction=None): Проверяет, можно ли двигаться в текущем направлении.
       update_position(): Обновляет позицию пакмана на основе текущего направления.
       is_portal(): Проверяет, находится ли пакман на портале.
       get_portal_positions(): Возвращает список позиций порталов.
       reverse_direction(direction): Возвращает обратное направление.
   """

   def __init__(self, pos_cell_x, pos_cell_y, direction, field):
       """
       Инициализирует объект класса PacmanMovement.

       Аргументы:
           pos_cell_x (int): Позиция пакмана по горизонтали.
           pos_cell_y (int): Позиция пакмана по вертикали.
           direction (tuple): Начальное направление движения.
           field (Field): Поле для проверки столкновений.
       """
       self.pos_cell_x = pos_cell_x
       self.pos_cell_y = pos_cell_y
       self.field = field  # поле (с методом get_array() для получения двумерного массива)
       self.direction = direction  # начальное направление

   def set_direction(self, direction):
       """
       Устанавливает новое направление движения.

       Аргументы:
           direction (tuple): Новое направление.
       """
       self.direction = direction

   def get_direction(self):
       """
       Возвращает текущее направление движения.

       Возвращает:
           tuple: Текущее направление.
       """
       return self.direction

   def can_move(self, direction=None):
       """
       Проверяет, можно ли двигаться в текущем направлении.

       Аргументы:
           direction (tuple, optional): Направление для проверки. Если не указано, используется текущее направление.

       Возвращает:
           bool: True, если можно двигаться, иначе False.
       """
       if direction is None:
           dx, dy = self.direction
       else:
           dx, dy = direction
       try:
           return self.field.to_array()[self.pos_cell_x + dx][self.pos_cell_y + dy] != "#"
       except IndexError:
           return False

   def update_position(self):
       """
       Обновляет позицию пакмана на основе текущего направления.
       """
       dx, dy = self.direction
       if self.can_move():
           self.pos_cell_x += dx
           self.pos_cell_y += dy

   def is_portal(self):
       """
       Проверяет, находится ли пакман на портале.

       Возвращает:
           bool: True, если пакман находится на портале, иначе False.
       """
       return self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == "T"

   def get_portal_positions(self):
       """
       Возвращает список позиций порталов.

       Возвращает:
           list: Список позиций порталов.
       """
       portal_positions = []
       for y in range(len(self.field)):  # Перебираем индексы строк
           for x in range(len(self.field[y])):  # Перебираем индексы столбцов
               if self.field.to_array()[x][y] == "T":  # Проверяем, есть ли "T" в текущей позиции
                   portal_positions.append((x, y))
       return portal_positions

   def reverse_direction(self, direction):
       """
       Возвращает обратное направление.

       Аргументы:
           direction (tuple): Направление.

       Возвращает:
           tuple: Обратное направление.
       """
       return (-direction[0], -direction[1])
   
class PacmanCollision:
    def __init__(self, pos_cell_x, pos_cell_y, field, pacman):
        self.pos_cell_x = pos_cell_x
        self.pos_cell_y = pos_cell_y
        self.field = field
        self.pacman = pacman
    
    def seed_collision(self):
        if self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == "." or self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == "S":
            return True
        return False
            
    def which_collision(self,weight):
        if self.field.to_array()[self.pos_cell_x][self.pos_cell_y] == ".":
            print("DEBUG: съел зерно")
            if weight == 10:
                if not self.pacman.turn_to_blue:
                    pr.play_sound(self.pacman.eating_corn_sound)
            elif weight == 20:
                if not self.pacman.turn_to_blue:
                    pr.set_sound_volume(self.pacman.turn_to_blue_sound, self.pacman.sound_volume)
                    self.pacman.turn_to_blue = True
                    self.pacman.turn_to_blue_start = pr.get_time()
                    self.pacman.turn_to_blue_end = self.pacman.turn_to_blue_start + 15
                    pr.play_sound(self.pacman.turn_to_blue_sound)