from base import Ghost

# Класс для красного привидения (Blinky)
class BlinkyGhost(Ghost):
    def change_direction(self, field):
        if self.dx == 0 and self.dy == 0:
            super().choose_direction()
