import random
import pygame
from settings import Settings

class Enviroment():
    '''All other objects whithout cells'''
    def __init__(self):
        self.settings = Settings()
        self.width = self.settings.start_size
        self.height = self.settings.start_size
        self.x = random.choice(list(range(int(self.settings.screen_width / self.settings.start_size))))
        self.y = random.choice(list(range(int(self.settings.screen_height / self.settings.start_size))))
        self.line_thin = self.settings.line_thin * 2


class Food(Enviroment):
    def __init__(self):
        super().__init__()
        self.type = 'food'
        self.color = self.settings.LIME
        self.object = pygame.Rect((self.x * self.width, self.y * self.height, self.width, self.height))
        self.energy = 5
