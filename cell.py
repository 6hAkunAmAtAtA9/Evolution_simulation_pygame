import random
import pygame
from settings import Settings

class Cell():

    def __init__(self, y, x, color, genome, kind, birth_coeff = 0):
        self.type = 'cell'
        self.settings = Settings()
        self.width = self.settings.start_size
        self.height = self.settings.start_size
        self.x = x
        self.y = y
        self.line_thin = self.settings.line_thin
        self.energy = self.settings.start_energy + int(birth_coeff) - 10
        self.action_possibility = False
        self.freedom_love = 0
        self.genome = genome
        self.kind = kind
        self.disabled_counter = self.settings.disabled_counter


        #self.color = random.choice(self.settings.colors)
        self.color = color
        self.object = pygame.Rect((self.x * self.width, self.y * self.height, self.width, self.height))
        self.step_counter = 0
        self.moving_leight = 0
        self.move_right_flag = False
        self.move_left_flag = False
        self.move_up_flag = False
        self.move_down_flag = False


