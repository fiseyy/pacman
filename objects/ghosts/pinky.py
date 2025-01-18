from base import Ghost

# Класс для розового привидения (Pinky)
class PinkyGhost(Ghost):
    def change_direction(self, field):
        # Pinky следует за Пакманом, но старается предвосхитить его движение
        if self.dx == 0 and self.dy == 0:
            # Например, Pinky может пытаться идти вперед на 4 клетки в направлении текущего движения Пакмана
            self.set_direction_based_on_target(field.target_x + 4 * field.target_dx,
                                               field.target_y + 4 * field.target_dy)