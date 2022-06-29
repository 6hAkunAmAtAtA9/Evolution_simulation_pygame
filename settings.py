import random


class Settings():

    def __init__(self):
        '''Cell settings'''

        self.cells_start_count = 10
        self.food_start_count = 0
        self.eat_coef = 1


        self.screen_width = 750
        self.screen_height = 750

        self.add_screen_width = self.screen_width
        self.add_screen_hight = self.screen_height # добавляет справа поле для изменения
        self.bg_color = (0, 0, 0)
        self.line_thin = 2
        self.start_size = 5  # начальный размер квадратов

        '''Indexing'''
        self.y_size = int(self.screen_height / self.start_size) - 1
        self.x_size = int(self.screen_width / self.start_size) - 1

        self.energy_coef = 0


        self.y_start_more_energy = self.screen_height // 7
        self.x_start_more_energy = self.screen_width // 7
        self.y_length_more_energy = self.screen_height - self.y_start_more_energy * 2
        self.x_length_more_energy = self.screen_width - self.x_start_more_energy * 2

        self.I_y_start_more_energy = int(self.y_start_more_energy / self.start_size) - 1
        self.I_x_start_more_energy = int(self.x_start_more_energy / self.start_size) - 1
        self.I_y_length_more_energy = int(self.y_length_more_energy / self.start_size) - 1
        self.I_x_length_more_energy = int(self.x_length_more_energy / self.start_size) - 1


        self.y_start_anymore_energy = self.screen_height // 3
        self.x_start_anymore_energy = self.screen_width // 3
        self.y_length_anymore_energy = self.screen_height - self.y_start_anymore_energy * 2
        self.x_length_anymore_energy = self.screen_width - self.x_start_anymore_energy * 2

        self.I_y_start_anymore_energy = int(self.y_start_anymore_energy / self.start_size) - 1
        self.I_x_start_anymore_energy = int(self.x_start_anymore_energy / self.start_size) - 1
        self.I_y_length_anymore_energy = int(self.y_length_anymore_energy / self.start_size) - 1
        self.I_x_length_anymore_energy = int(self.x_length_anymore_energy / self.start_size) - 1


        '''Colors'''
        self.colors = ["light blue", "spring green", "golden rod",
                       "lime", 'aqua', 'royal blue', "yellow", "red", "blue",
                       'DarkSalmon', 'MediumSpringGreen', "MidnightBlue", "SlateBlue",
                       'DarkOrange', 'DeepSkyBlue', 'Chocolate', 'Gray', 'LightSlateGray']

        '''Cell life settings'''
        self.len_genome = 15
        self.start_energy = random.randint(50, 100)  # потом поменять вернуть 10,60
        self.life_time = 100
        self.free_place_needing = 4  # максимально количество клеток рядом
        self.disabled_counter = 10

        # self.genime_case =
