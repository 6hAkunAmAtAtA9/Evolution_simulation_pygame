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

        self.kinds = [chr(i) + str(j) for i in range(65, 91) for j in range(1, 100)]

        for _ in range(self.settings.cells_start_count):
            self.birth()

        for i in range(self.settings.food_start_count):
            food = Food()
            if self.objects[food.y][food.x] == '0':
                self.objects[food.y][food.x] = food

        self.round_counter = 0
        self.death_count = 0
        self.cell_count = 0
        self.kinds_uniq = {}

    def run_game(self):
        while True:
            self.cell_count = 0
            self.kinds_uniq = {}
            self.screen.fill(self.settings.bg_color)
            self.round_counter += 1

            if self.round_counter % 20 == 0:
                self.birth()



            '''Проход основного цикла жизни с переработкой массива  координат клеток'''
            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell' and self.objects[i][j].action_possibility == True:
                            if self.objects[i][j].kind not in self.kinds_uniq.keys():
                                self.kinds_uniq[self.objects[i][j].kind] = 1
                            else:
                                self.kinds_uniq[self.objects[i][j].kind] += 1
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



            pygame.display.flip()
            time.sleep(0.1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            '''Выводим в консоль количество клеток каждого вида'''
            sorted_tuples = sorted(self.kinds_uniq.items(), key=lambda item: item[1], reverse=True)
            sorted_dict = {k: v for k, v in sorted_tuples}
            print(sorted_dict)
            # print('ROUND')
            # print(self.cell_count)

    def birth(self):
        a = random.randint(0, len(self.objects) - 1)
        b = random.randint(0, len(self.objects[0]) - 1)
        kind = self.kinds.pop(0)
        if self.objects[a][b] == '0':
            try:
                self.objects[a][b] = Cell(a, b, random.choice(self.settings.colors), self.genome(), kind)
            except IndexError:
                pass


    def genome(self):
        a = []
        # while len(a) < 10:
        #     a.append(random.choice(("up", 'down', 'right', 'left')))
        a.append('birth')
        while len(a) < 25:
            a.append('none')
        random.shuffle(a)
        return a

if __name__ == "__main__":
    eg = Evolution_game()
    eg.run_game()
