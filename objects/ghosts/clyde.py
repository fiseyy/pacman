from base import Ghost
# Класс для оранжевого привидения (Clyde)
class ClydeGhost(Ghost):
    def change_direction(self, field):
        # Clyde меняет стратегию в зависимости от расстояния до Пакмана
        if self.dx == 0 and self.dy == 0:
            distance_to_pacman = ((self.x - field.target_x) ** 2 + (self.y - field.target_y) ** 2) ** 0.5
            if distance_to_pacman > 8:
                # Если далеко, то преследует Пакмана
                self.set_direction_based_on_target(field.target_x, field.target_y)
            else:
                # Если близко, то убегает
                self.choose_direction_away_from(field.target_x, field.target_y)