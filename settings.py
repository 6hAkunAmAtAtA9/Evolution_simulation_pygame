import random

class Settings():

    def __init__(self):
        self.cells_start_count = 3
        self.food_start_count = 5
        self.screen_width = 100
        self.screen_height = 100
        self.bg_color = (0, 0, 0)
        self.line_thin = 5
        self.start_size = 20   # начальный размер квадратов
        self.start_energy = 30

        '''Colors'''
        self.LIGHT_BLUE = (173, 216, 230)
        self.SPRING_GREEN = (0, 255, 127)
        self.GOLDEN_ROD = (218, 165, 32)
        self.CRIMZON = (220, 20, 60)
        self.VIOLET = (238, 130, 238)
        self.MIST_ROSE = (255, 228, 225)
        self.LIME = (0, 255, 0)
        self.AQUA = (0, 255, 255)
        self.ROYAL_BLUE = (65, 105, 225)
        self.colors = [self.LIGHT_BLUE, self.SPRING_GREEN, self.GOLDEN_ROD,
                       self.CRIMZON, self.LIME, self.AQUA]
