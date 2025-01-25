from objects.ghosts.base import Ghost
import random
class InkyGhost(Ghost):
    def __init__(self, x=0, y=0, cell_size=10, field=None, textures=None, pacman=None):
        time_to_movement_since_start = 7
        self.pacman = pacman
        super().__init__(x, y, cell_size=cell_size, field=field, textures=textures.get_texture("inky"), time_to_movement_since_start=time_to_movement_since_start)

    def set_target(self):
        self.target_x = self.pacman.pos_cell_x
        self.target_y = self.pacman.pos_cell_y

    def define_target_direction(self):
        if self.target_x > self.pos_cell_x:
            return tuple((1,0))
        elif self.target_x < self.pos_cell_x:
            return tuple((-1,0))
        elif self.target_y > self.pos_cell_y:
            return tuple((0,1))
        elif self.target_y < self.pos_cell_y:
            return tuple((0,-1))
        else:
            return tuple((0,0))
        
    def change_direction(self):
        self.set_target()
        if not self.movement.can_move(self.define_target_direction()[0], self.define_target_direction()[1]):
            self.movement.choose_new_direction()  # Если не можем двигаться к цели, выбираем новое направление
        else:
            self.movement.set_direction_based_on_target(self.target_x, self.target_y)