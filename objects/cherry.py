import pyray as pr
import time
"""библиотека для использования времени"""
class Cherry:
    """класс вишенки
    когда хотим показать вишенку, вызывается функция show она делает параметр self.is_alive=True и засекает время,
    что позволяет в дальнейшем работать с функцией logic() (вызывается в основном цикле всегда при отрисовке), 
    чтобы вишенку скрыть требуется вызов функции hide()"""
    def __init__(self,x,y,r):
        """конструктор класса

        Args:
            x (int): координата x вишенки
            y (int): координата y вишенки
            r (int): радиус вишенки
        """
        self.x=x
        self.y=y
        self.r=r
        self.SHOW_TIME=3
        self.HIDE_TIME=5
        self.start_time=pr.get_time()
        self.is_alive = False

    def show(self):
        """показывает вишенку через 5 секунд"""
        self.is_alive=True
        self.start_time=pr.get_time()
        
    
    def hide(self):
        """скрывает вишенку"""
        self.is_alive=False
    
    def logic(self):
        """показывает через 3 сек скрывает через 5 сек"""
        if not(self.is_alive):
            return
        time_now=-self.start_time+pr.get_time()
        if time_now>=self.SHOW_TIME and time_now<=self.HIDE_TIME+self.SHOW_TIME:
            pr.draw_circle(self.x,self.y,self.r,pr.RED)