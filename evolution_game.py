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


        for i in range(self.settings.cells_start_count):
            cell = Cell()
            if self.objects[cell.x][cell.y] == '0':
                self.objects[cell.x][cell.y] = cell

        for i in range(self.settings.food_start_count):
            food = Food()
            if self.objects[food.x][food.y] == '0':
                self.objects[food.x][food.y] = food
        #
        # for i in range(self.settings.cells_start_count, self.settings.cells_start_count + self.settings.food_start_count):
        #     env = Food()
        #         self.objects[i] = env
        #     if actions.movement_possibility(env, self.objects):

        self.round_counter = 0
        #print(self.objects)
        #print(dir(self.objects[0]))
        #print(self.objects[0].type)

        #for value in self.objects.values():
            #print(f'{value.type} in {value.x}:{value.y}')


    def run_game(self):
        while True:
            self.screen.fill(self.settings.bg_color)


            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        print(self.objects[i][j].x, self.objects[i][j].y)
                        pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object, self.objects[i][j].line_thin)


            # actions.killer(self.objects)
            # for key, value in self.objects.items():
            #     if value.type == 'cell':
            #         actions.life_cicle(value, self.objects)
            #         pygame.draw.rect(self.screen, value.color, value.object, self.settings.line_thin)
            #
            #     if value.type == 'food':
            #         pygame.draw.rect(self.screen, value.color, value.object, value.line_thin)

            for i in range(len(self.objects)):
                print(self.objects[i])



            print("*" * len(self.objects))



            pygame.display.flip()

            time.sleep(60)
            self.round_counter += 1



            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()


if __name__ == "__main__":
    eg = Evolution_game()
    eg.run_game()





