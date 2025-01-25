from objects.ghosts.base import Ghost, GhostMovement
import pyray as pr

class InkyGhost(Ghost):
    def __init__(self, x=0, y=0, cell_size=10, field=None, textures=None):
        super().__init__(x, y,cell_size=cell_size, field=field, textures=textures.get_texture("inky"))