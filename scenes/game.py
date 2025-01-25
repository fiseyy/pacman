import pyray as pr
from scenes.base import SceneBase
from objects.cherry import Cherry
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT, load_settings
from objects.field import FieldDrawer
from objects.textures import Textures
from logic.field import Field
from objects.ghosts.inky import InkyGhost
from objects.ghosts.clyde import ClydeGhost
from objects.ghosts.blinky import BlinkyGhost
from objects.ghosts.pinky import PinkyGhost
from objects.images.pacman import Pacman
from objects.score import ScoreDrawer
from logic.score import ScoreCounter
from logic.life import LifeCounter
from objects.life import LifeDrawer
class GameScene(SceneBase):
    """
   Класс для игровой сцены.

   Методы:
       enter(): Входит в игровую сцену.
       draw(): Рисует игровую сцену.
    """
    def __init__(self,state,cell_size, life_counter, score_counter):
        self.state = state
        self.x_to_center = 0
        self.y_to_center = 0
        # подключение звуков
        self.game_over_sound = pr.load_sound("sounds/game/game_over.mp3")
        self.ghosts_moving_sound = pr.load_sound("sounds/game/ghosts_moving.mp3")
        self.start_game_sound = pr.load_sound("sounds/game/start_game.mp3")
        self.eating_fruit_sound = pr.load_sound("sounds/game/eating_fruit.mp3")
        # pr.set_sound_volume(self.eating_fruit_sound, 0.5)
        self.ghosts_moving_sound_playing = False  # Флаг для отслеживания воспроизведения звука
        self.sound_start_time = 0  # Время начала воспроизведения звука

        self.textures = Textures()
        self.field = Field("objects/maps/field.txt")
        self.pacman = Pacman(1,1,cell_size, self.textures.get_texture("pacman"),self.field)
        self.field_drawer = FieldDrawer(self.field,cell_size)
        self.blinky_ghost = BlinkyGhost(x=14, y=14,cell_size=cell_size, field=self.field,textures=self.textures, pacman=self.pacman)
        self.pinky_ghost = PinkyGhost(x=14, y=14,cell_size=cell_size, field=self.field,textures=self.textures, pacman=self.pacman)
        self.clyde_ghost = ClydeGhost(x=14, y=14,cell_size=cell_size, field=self.field,textures=self.textures, pacman=self.pacman)
        self.inky_ghost = InkyGhost(x=14, y=14,cell_size=cell_size, field=self.field,textures=self.textures, pacman=self.pacman)
        self.cherry=Cherry(1,3,5,cell_size, self.textures.get_texture("cherry"))
        self.cherry_eaten = False
        if not life_counter:
            self.life_counter = LifeCounter(initial_lives=3)
        else:
            self.life_counter = life_counter
        if not score_counter:
            self.score_counter = ScoreCounter(initial_score=0)
        else:
            self.score_counter = score_counter
        # self.score_counter = ScoreCounter(initial_score=0)
        self.score_drawer = ScoreDrawer(SCREEN_WIDTH - 145, 10, self.score_counter)
        # self.life_counter = LifeCounter()
        self.life_drawer = LifeDrawer(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 25, self.textures.get_texture("life"))
        self.pacman_death = False
        self.death_time = None
        self.start_time = pr.get_time()
        pr.play_sound(self.start_game_sound)
        super().__init__()
    def debug_add_remove_score(self): # DEBUG METHOD
        if pr.is_key_pressed(pr.KEY_UP):
            self.score_counter.add(10)
        elif pr.is_key_pressed(pr.KEY_DOWN):
            self.score_counter.remove(5)
    def debug_add_remove_lifes(self): # DEBUG METHOD
        if pr.is_key_pressed(pr.KeyboardKey.KEY_RIGHT):
            self.life_counter.add()
        elif pr.is_key_pressed(pr.KeyboardKey.KEY_LEFT):
            self.life_counter.remove()
    def restart_game(self):
        self.state.restart_game()
    def enter(self):
        """
       Входит в игровую сцену.
        """
        print("Entering Game Scene")
        self.cherry.start()
    def draw(self):
        """
       Рисует игровую сцену.
        """
        if pr.get_time() - self.start_time >= 4.5:
            pr.clear_background(BLACK_BACKGROUND)
            #pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, 5), FONT_SIZE, 1.0, WHITE_TEXT)
            self.field_drawer.draw(self.x_to_center, self.y_to_center)
            self.process_additional_logic()  # Обработка дополнительной логики
            self.cherry.draw() # Рисуем Cherry
            self.pacman.draw() # Рисуем Pacman
            self.score_drawer.draw() # Рисуем очки
            self.life_drawer.draw(self.life_counter.get_lives()) # Рисуем жизни
            self.debug_add_remove_score() # на стрелочку вверх/вниз можно увеличивать / уменьшать очки (DEBUG FEATURE)
            self.debug_add_remove_lifes() # на стрелочку влево/вправо можно увеличивать / уменьшать жизни (DEBUG FEATURE)
            self.clyde_ghost.draw()    # Рисуем Clyde
            self.inky_ghost.draw()    # Рисуем Inky
            self.blinky_ghost.draw()
            self.pinky_ghost.draw()
        else:
            pr.clear_background(BLACK_BACKGROUND)
            self.field_drawer.draw(self.x_to_center, self.y_to_center)
            self.pacman.draw()
            self.score_drawer.draw()
            self.life_drawer.draw(self.life_counter.get_lives())
            self.debug_add_remove_score()
            self.debug_add_remove_lifes()
            self.clyde_ghost.draw()    # Рисуем Clyde
            self.inky_ghost.draw()    # Рисуем Inky
            self.blinky_ghost.draw()
            self.pinky_ghost.draw()
        
    def process_additional_logic(self):
    # Проверяем, не мертв ли Пакман
        if not self.pacman_death:
            self.cherry.logic()
            for seed in self.field_drawer.seeds:
                seed.collisions(self.pacman, self.score_counter)

            # Проверка столкновения с призраками
            if not self.pacman_death:
                if self.clyde_ghost.movement.check_collision_with_pacman(self.pacman):
                    if self.pacman.turn_to_blue:
                        self.clyde_ghost.movement.died()
                    else:
                        if self.clyde_ghost.spawn_time < pr.get_time():
                            self.pacman_death = True
            self.clyde_ghost.update()  # Обновляем состояние Clyde

            if not self.pacman_death:
                if self.inky_ghost.movement.check_collision_with_pacman(self.pacman):
                    if self.pacman.turn_to_blue:
                        self.inky_ghost.movement.died()
                    else:
                        if self.clyde_ghost.spawn_time < pr.get_time():
                            self.pacman_death = True
            self.inky_ghost.update()  # Обновляем состояние Inky

            if not self.pacman_death:
                if self.blinky_ghost.movement.check_collision_with_pacman(self.pacman):
                    if self.pacman.turn_to_blue:
                            self.blinky_ghost.movement.died()
                    else:
                            if self.clyde_ghost.spawn_time < pr.get_time():
                                self.pacman_death = True
            self.blinky_ghost.update()

            if not self.pacman_death:
                if self.pinky_ghost.movement.check_collision_with_pacman(self.pacman):
                    if self.pacman.turn_to_blue:
                            self.pinky_ghost.movement.died()
                    else:
                            if self.clyde_ghost.spawn_time < pr.get_time():
                                self.pacman_death = True
            self.pinky_ghost.update()

            # Пакман
            self.pacman.define_direction()
            self.pacman.move()

            # пакман и вишня
            if self.cherry.collision(self.pacman):
                if not self.cherry_eaten:
                    self.cherry.hide()
                    self.score_counter.add(100)
                    self.cherry_eaten = True
                    pr.play_sound(self.eating_fruit_sound)
            else:
                self.cherry_eaten = False
            
            if self.blinky_ghost.movement.is_moving() or self.clyde_ghost.movement.is_moving() or self.inky_ghost.movement.is_moving() or self.pinky_ghost.movement.is_moving():
                if not self.pacman_death and not self.ghosts_moving_sound_playing:
                    pr.play_sound(self.ghosts_moving_sound)
                    self.ghosts_moving_sound_playing = True
                    self.sound_start_time = pr.get_time()  # Запоминаем время начала воспроизведения
            else:
                self.ghosts_moving_sound_playing = False  # Если призраки не двигаются, сбрасываем флаг
            # Проверяем, истекло ли время воспроизведения звука
            if self.ghosts_moving_sound_playing and (pr.get_time() - self.sound_start_time >= 03.998):
                self.ghosts_moving_sound_playing = False  # Сбрасываем флаг, если звук закончился

            if self.pacman_death:
                pr.set_sound_volume(self.ghosts_moving_sound, 0)
                pr.play_sound(self.game_over_sound)
                self.life_counter.remove()
                self.death_time = pr.get_time()
                self.pacman.death_animation()
            if self.pacman.turn_to_blue_start != None:
                if self.pacman.turn_to_blue_end < pr.get_time():
                    pr.set_sound_volume(self.pacman.turn_to_blue_sound, 0)
                    self.pacman.turn_to_blue = False
                elif pr.get_time() - self.pacman.turn_to_blue_start >= 4.83:
                    pr.play_sound(self.pacman.turn_to_blue_sound)
                    self.pacman.turn_to_blue_start = pr.get_time()
                    self.blinky_ghost.afraid = True
                    self.clyde_ghost.afraid = True
                    self.inky_ghost.afraid = True
                    self.pinky_ghost.afraid = True
                else:
                    self.blinky_ghost.afraid = True
                    self.clyde_ghost.afraid = True
                    self.inky_ghost.afraid = True
                    self.pinky_ghost.afraid = True

        # Логика обработки смерти
        if self.death_time:
            
            if self.death_time + 3 < pr.get_time():
                if self.life_counter.get_lives() == 0:
                    # TODO: здесь сохранять результаты в таблицу рекордов
                    # self.state.restart_game(0,0)
                    self.state.game_over(self.score_counter.get_score())
                else:
                    # self.pacman_death = False
                    # self.pacman.alive()
                    # self.field.ghost_spawners.reset()
                    # self.clyde_ghost.restart()
                    # self.inky_ghost.restart()
                    self.state.restart_game(self.life_counter, self.score_counter)
            else:
                self.pacman.death_animation_drawer()
        if self.field_drawer.get_seeds() == []:
            # Level completed
            self.state.restart_game(self.life_counter, self.score_counter)