import random


class Settings():

    def __init__(self):
        '''Cell settings'''

        self.cells_start_count = 10
        self.food_start_count = 0
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.line_thin = 2
        self.start_size = 2  # начальный размер квадратов

        '''Indexing'''
        self.y_size = int(self.screen_height / self.start_size) - 1
        self.x_size = int(self.screen_height / self.start_size) - 1

        '''Colors'''

        self.colors = ["light blue", "spring green", "golden rod",
                       "lime", 'aqua', 'royal blue', "yellow", "red", "blue"]

        '''Cell life settings'''
        self.start_energy = random.randint(10, 30)  # потом поменять
        self.free_place_needing = 7   # стандартно 5
