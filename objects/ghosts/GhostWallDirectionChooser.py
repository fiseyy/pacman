import random

"""класс ghost оставляю как тестировочный без него прога не будет работать"""
class Ghost:
    def __init__(self, x=0, y=0, direction=(0, 1), width=10, height=10):
        self.__x: int = x
        self.__y: int = y
        self.__direction = direction
        self.__width: int = 10
        self.__height: int = 10

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_direction(self):
        return self.__direction

    def set_direction(self, direction):
        self.__direction = direction

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

"""класс включает в себя определение напрвления на перекрёстке"""
class GhostWallDirectionChooser:
    """
    определение направления приведения
    """
    def __init__(self, ghost: Ghost, field):
        """конструктор

        Args:
            ghost (Ghost): приведение(объект класса)
            field (_type_): поле (двумерный список)
        """
        self.ghost = ghost
        self.number_pixsels_in_cell_x = 10
        self.number_pixsels_in_cell_y = 10
        self.d = ghost.get_direction()
        self.x = ghost.get_x() // self.number_pixsels_in_cell_x
        self.y = ghost.get_x() // self.number_pixsels_in_cell_y
        self.field = field

    def dminus(self, d: tuple):
        """функция для поворота приведения против часовой стрелки

        Args:
            d (tuple): кортеж из 2 элементов, показывает в какую сторону направлено приведение

        Returns:
            _type_: кортеж из 2 элементов, новое направление
        """
        x = d[0]
        y = d[1]
        if x == -1 and y == 0:
            return tuple(0, 1)
        if x == 0 and y == 1:
            return tuple(1, 0)
        if x == 1 and y == 0:
            return tuple(0, -1)
        if x == 0 and y == -1:
            return tuple(-1, 0)

    def dplus(self, d):
        """функция для поворота приведения по часовой стрелки

        Args:
            d (_type_): кортеж из 2 элементов, показывает в какую сторону направлено приведение

        Returns:
            _type_: кортеж из 2 элементов, новое направление
        """
        x = d[0]
        y = d[1]
        if x == -1 and y == 0:
            return (0, -1)
        if x == 0 and y == -1:
            return (1, 0)
        if x == 1 and y == 0:
            return (0, 1)
        if x == 0 and y == 1:
            return (-1, 0)

    def change_direction(self, x, y, direction) -> None:
        """Изменяет направление

        Args:
            x (_type_): координата x приведения
            y (_type_): координата y приведения
            direction (_type_): кортеж из 2 элементов
        """
        if self.x % self.number_pixsels_in_cell_x != 0:
            return
        if self.y % self.number_pixsels_in_cell_y != 0:
            return
        self.x = self.ghost.get_x() // self.number_pixsels_in_cell_x
        self.y = self.ghost.get_x() // self.number_pixsels_in_cell_y
        self.d = direction
        if self.field[self.x + self.d[0]][self.y + self.d[1]] == "#":
            if self.field[self.dminus(self.d)[0]][self.dminus(self.d)[1]] == "#":
                if self.field[self.dplus(self.d)[0]][self.dplus(self.d)[1]] == "#":
                    self.ghost.set_direction((-self.d[0], -self.d[1]))
                else:
                    self.ghost.set_direction((self.dminus(self.d)[0], self.dminus(self.d)[1]))
            elif self.field[self.dplus(self.d)[0]][self.dplus(self.d)[1]] == "#":
                self.ghost.set_direction((self.dminus(self.d)[0], self.dminus(self.d)[1]))
                
            else:
                self.ghost.set_direction((self.dminus(self.d)[0], self.dminus(self.d)[1]))
        elif not (self.field[self.dminus(self.d)[0]][self.dminus(self.d)[1]] == "") and not (
                self.field[self.dplus(self.d)[0]][self.dplus(self.d)[1]] == ""):
            self.ghost.set_direction(self.x + self.d[0], y + self.d[1])  