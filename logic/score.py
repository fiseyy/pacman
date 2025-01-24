class ScoreCounter:
    def __init__(self, initial_score=0):
        """
        Инициализирует счётчик очков с заданным начальным значением.
        
        :param initial_score: Начальное количество очков (по умолчанию 0).
        """
        self.score = initial_score

    def add(self, points):
        """
        Увеличивает количество очков на заданное значение.
        
        :param points: Количество очков для добавления.
        """
        self.score += points

    def remove(self, points):
        """
        Уменьшает количество очков на заданное значение, если это возможно.
        
        :param points: Количество очков для удаления.
        """
        if self.score >= points:
            self.score -= points
        else:
            # Ставим очки в ноль, если недостаточно для удаления
            self.score = 0

    def get_score(self):
        """
        Возвращает текущее количество очков.
        
        :return: Количество оставшихся очков.
        """
        return self.score