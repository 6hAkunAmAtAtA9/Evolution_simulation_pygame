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
            b = random.randint(0, len(self.objects[0]))
            arr.append((a, b))



        for i in range(len((self.objects))):
            for j in range(len(self.objects[i])):
                if (i, j) in arr and self.objects[i][j] == '0':
                    color = random.choice(self.settings.colors)
                    self.objects[i][j] = Cell(i, j, color, {'Желание_жить': 1})

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
            self.cell_count = 0
            self.screen.fill(self.settings.bg_color)
            self.round_counter += 1

            '''Прохож основного цикла жизни с переработкой массива  координат клеток'''
            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell' and self.objects[i][j].action_possibility == True:
                            actions.life_cicle(self.objects[i][j], self.objects)

            """Отрисовка нового масива"""
            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell':
                            self.cell_count += 1
                            self.objects[i][j].action_possibility = True
                            self.cell_count += 1
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)
                        else:
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)

            if self.round_counter % 20 == 0:
                a = random.randint(0, len(self.objects))
                b = random.randint(0, len(self.objects[0]))
                try:
                    self.objects[a][b] = Cell(a, b, random.choice(self.settings.colors), {'Желание_жить': 1})
                except IndexError:
                    pass


            pygame.display.flip()
            time.sleep(0.1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            print('ROUND')


if __name__ == "__main__":
    eg = Evolution_game()
    eg.run_game()
