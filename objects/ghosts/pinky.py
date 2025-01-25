from objects.ghosts.base import Ghost

# Класс для розового привидения (Pinky)
class PinkyGhost(Ghost):
    def __init__(self, x=0, y=0, cell_size=10, field=None, textures=None, pacman=None):
        time_to_movement_since_start = 10
        self.pacman = pacman
        super().__init__(x, y, cell_size=cell_size, field=field, textures=textures.get_texture("pinky"), time_to_movement_since_start=time_to_movement_since_start)

    def set_target(self):
        self.target_x = self.pacman.pos_cell_x
        self.target_y = self.pacman.pos_cell_y
        if self.afraid:
            self.target_x *= -1
            self.target_y *= -1
    def define_target_direction(self):
        res = tuple()
        if self.target_x > self.pos_cell_x:
            res = tuple((1,0))
        elif self.target_x < self.pos_cell_x:
            res = tuple((-1,0))
        elif self.target_y > self.pos_cell_y:
            res = tuple((0,1))
        elif self.target_y < self.pos_cell_y:
            res = tuple((0,-1))
        return res
    def change_direction(self):
        self.set_target()
        # сторона, в которую надо идти
        self.movement.set_direction(self.define_target_direction()) 
        if not self.movement.can_move():
            self.movement.choose_new_direction()  # Если не можем двигаться к цели, выбираем новое направление
        else:
            self.movement.set_direction_based_on_target(self.target_x, self.target_y)