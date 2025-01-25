import pyray as pr
from scenes.base import SceneBase
from objects.cherry import Cherry
from settings import BLACK_BACKGROUND, font, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE, WHITE_TEXT
from objects.field import FieldDrawer
from objects.textures import Textures
from logic.field import Field
from objects.ghosts.inky import InkyGhost
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
    def __init__(self,cell_size):
        self.x_to_center = 0
        self.y_to_center = 0
        self.textures = Textures()
        self.field = Field("objects/maps/field.txt")
        self.pacman = Pacman(1,1,cell_size, self.textures.get_texture("pacman"),self.field)
        self.field_drawer = FieldDrawer(self.field,cell_size)
        self.inky_ghost = InkyGhost(x=1, y=1,cell_size=cell_size, field=self.field,textures=self.textures)
        self.cherry=Cherry(1,2,5,cell_size)
        self.score_counter = ScoreCounter(initial_score=0)
        self.score_drawer = ScoreDrawer(SCREEN_WIDTH - 145, 10, self.score_counter)
        self.life_counter = LifeCounter()
        self.life_drawer = LifeDrawer(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 25, self.textures.get_texture("life"))
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
        
        pr.clear_background(BLACK_BACKGROUND)
        #pr.draw_text_ex(font, "Game Scene", (SCREEN_WIDTH // 2 - 100, 5), FONT_SIZE, 1.0, WHITE_TEXT)
        self.field_drawer.draw(self.x_to_center, self.y_to_center)
        self.process_additional_logic()  # Обработка дополнительной логики
        self.inky_ghost.update()  # Обновляем состояние Inky
        self.inky_ghost.draw()    # Рисуем Inky
        self.cherry.draw() # Рисуем Cherry
        self.pacman.draw() # Рисуем Pacman
        self.score_drawer.draw() # Рисуем очки
        self.life_drawer.draw(self.life_counter.get_lives()) # Рисуем жизни
        self.debug_add_remove_score() # на стрелочку вверх/вниз можно увеличивать / уменьшать очки (DEBUG FEATURE)
        self.debug_add_remove_lifes() # на стрелочку влево/вправо можно увеличивать / уменьшать жизни (DEBUG FEATURE)
        
    def process_additional_logic(self):
        # self.inky_ghost.change_direction(self.field)
        self.cherry.logic()
        self.pacman.define_direction()
        self.pacman.move()
        for seed in self.field_drawer.seeds:
            seed.collisions(self.pacman, self.score_counter)
        
    
        