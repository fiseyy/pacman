class LifeCounter:
    def __init__(self, initial_lives=3):
        """
        Инициализирует счётчик жизней с заданным количеством жизней.
        
        :param initial_lives: Начальное количество жизней (по умолчанию 3).
        """
        self.lives = initial_lives

    def add(self):
        """
        Увеличивает количество жизней на 1.
        
        Этот метод используется, когда игрок получает дополнительную жизнь.
        """
        self.lives += 1

    def remove(self):
        """
        Уменьшает количество жизней на 1, если они больше 0.
        
        Этот метод вызывается, когда игрок теряет жизнь. 
        Если жизни уже на нуле, метод ничего не делает.
        """
        if self.lives > 0:
            self.lives -= 1

    def get_lives(self):
        """
        Возвращает текущее количество жизней.
        
        :return: Количество оставшихся жизней.
        
        """
        return self.lives
    def isAlive(self)->bool:
        if self.lives==0:
            return False
        return True 