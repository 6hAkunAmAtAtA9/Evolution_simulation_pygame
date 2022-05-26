import pygame
import sys
import time
import random
from settings import Settings
from cell import Cell
from environemt import Enviroment, Food
import actions


class Evolution_game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Square")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.objects = [['0' for _ in range(int(self.settings.screen_width / self.settings.start_size))]
                        for _ in range(int(self.settings.screen_height / self.settings.start_size))]


        arr = []
        for _ in range(self.settings.cells_start_count):
            a = random.randint(0, len(self.objects))
            b = random.randint(0, len(self.objects))
            arr.append((a, b))
        print(arr)


        for i in range(len((self.objects))):
            for j in range(len(self.objects[i])):
                if (i, j) in arr and self.objects[i][j] == '0':
                    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    self.objects[i][j] = Cell(i,j, color)

        for i in range(self.settings.food_start_count):
            food = Food()
            if self.objects[food.y][food.x] == '0':
                self.objects[food.y][food.x] = food

        self.round_counter = 0
        self.death_count = 0
        self.cell_count = 0

        print('Y:', len(self.objects), 'X:', len(self.objects[0]))

    def run_game(self):
        while True:
            self.screen.fill(self.settings.bg_color)
            actions.killer(self.objects, self.death_count)


            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell' and self.objects[i][j].action_possibility == True:
                            actions.life_cicle(self.objects[i][j], self.objects)


            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell':
                            self.objects[i][j].action_possibility = True
                            self.cell_count += 1
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)
                        else:
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)

            pygame.display.flip()
            time.sleep(0.1)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == "__main__":
    eg = Evolution_game()
    eg.run_game()
