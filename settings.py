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
        self.start_size = 5  # начальный размер квадратов

        '''Indexing'''
        self.y_size = int(self.screen_height / self.start_size) - 1
        self.x_size = int(self.screen_height / self.start_size) - 1

        '''Colors'''

        self.colors = ["light blue", "spring green", "golden rod",
                       "lime", 'aqua', 'royal blue', "yellow", "red", "blue",
                       'DarkSalmon', 'MediumSpringGreen', "MidnightBlue", "SlateBlue",
                       'DarkOrange', 'DeepSkyBlue', 'Chocolate', 'Gray', 'LightSlateGray']

        '''Cell life settings'''
        self.start_energy = random.randint(10, 60)  # потом поменять вернуть 10,60
        self.free_place_needing = 4   # максимально количество клеток рядом
