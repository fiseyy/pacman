from base import Ghost
# Класс для голубого привидения (Inky)
class InkyGhost(Ghost):
    def change_direction(self, field):
        # Inky использует более сложную стратегию, основанную на позиции других приведений
        if self.dx == 0 and self.dy == 0:
            # Например, Inky может двигаться к точке, рассчитанной на основе позиции Пакмана и Blinky
            target_x = 2 * field.target_x - field.blinky_x
            target_y = 2 * field.target_y - field.blinky_y
            self.set_direction_based_on_target(target_x, target_y)