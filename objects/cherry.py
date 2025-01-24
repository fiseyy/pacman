import pyray as pr
import time

class Cherry:
    def __init__(self, x, y, r, cell_size):
        self.x = x * cell_size
        self.y = y * cell_size
        self.r = r
        self.SHOW_TIME = 3
        self.HIDE_TIME = 10
        self.start_time = pr.get_time()
        self.is_alive = False
        self.cell_size = cell_size
        self.state = 'hidden'  # 'hidden' or 'visible'
        self.start_delay = 10  # время задержки перед первым показом
        self.initial_start_time = pr.get_time()  # время запуска

    def show(self):
        self.is_alive = True
        self.start_time = pr.get_time()
        self.state = 'visible'

    def hide(self):
        self.is_alive = False
        self.state = 'hidden'

    def logic(self):
        current_time = pr.get_time() - self.start_time
        
        if self.state == 'visible':
            if current_time >= self.SHOW_TIME:
                self.hide()
        else:  # state is 'hidden'
            if current_time >= self.HIDE_TIME:
                self.show()

    def draw(self):
        if self.is_alive:
            pr.draw_circle(self.x + self.cell_size // 2, self.y + self.cell_size // 2, self.r, pr.RED)

    def start(self):
        # Проверяем, прошло ли 10 секунд с момента запуска
        if pr.get_time() - self.initial_start_time >= self.start_delay:
            self.show()