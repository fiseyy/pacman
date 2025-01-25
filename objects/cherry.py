import pyray as pr

class Cherry:
    def __init__(self, x, y, r, cell_size,texture):
        self.pos_x = x
        self.pos_y = y
        self.pos_cell_x = x * cell_size
        self.pos_cell_y = y * cell_size
        self.r = r
        self.SHOW_TIME = 10
        self.HIDE_TIME = 30
        self.start_time = pr.get_time()
        self.is_alive = False
        self.cell_size = cell_size
        self.state = 'hidden'  # 'hidden' or 'visible'
        self.start_delay = 40  # время задержки перед первым показом
        self.initial_start_time = pr.get_time()  # время запуска
        self.texture = texture

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
            # pr.draw_circle(self.pos_cell_x + self.cell_size // 2, self.pos_cell_y + self.cell_size // 2, self.r, pr.RED)
            pr.draw_texture(self.texture, self.pos_cell_x, self.pos_cell_y, pr.WHITE)
    def collision(self,pacman):
        return self.pos_x == pacman.pos_cell_x  and self.pos_y == pacman.pos_cell_y
            
    def start(self):
        # Проверяем, прошло ли 10 секунд с момента запуска
        if pr.get_time() - self.initial_start_time >= self.start_delay:
            self.show()