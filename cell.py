import random
import pygame
from settings import Settings

class Cell():

    def __init__(self):
        self.type = 'cell'

        self.settings = Settings()
        self.width = self.settings.start_size
        self.height = self.settings.start_size
        self.x = random.choice(list(range(int(self.settings.screen_width / self.settings.start_size))))
        self.y = random.choice(list(range(int(self.settings.screen_height / self.settings.start_size))))
        self.line_thin = self.settings.line_thin
        self.energy = self.settings.start_energy

        #self.color = random.choice(self.settings.colors)
        self.color = self.settings.ROYAL_BLUE
        self.object = pygame.Rect((self.y * self.height, self.x * self.width, self.width, self.height))
        self.step_counter = 0
        self.moving_leight = 0
        self.move_right_flag = False
        self.move_left_flag = False
        self.move_up_flag = False
        self.move_down_flag = False


