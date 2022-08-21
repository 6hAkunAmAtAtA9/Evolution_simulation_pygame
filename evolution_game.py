import pygame
import sys
import time
import random
from settings import Settings
from cell import Cell
import actions
from button import Button
from info import info


class Evolution_game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Square")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.add_screen_width, self.settings.add_screen_hight))

        self.objects = [['0' for _ in range(int(self.settings.screen_width / self.settings.start_size))]
                        for _ in range(int(self.settings.screen_height / self.settings.start_size))]

        self.kinds = [chr(i) + str(j) for i in range(65, 91) for j in range(100, 1000)]

        for _ in range(self.settings.cells_start_count):
            self.birth()

        self.round_counter = 0
        self.death_count = 0
        self.mutation_count = 0
        self.birth_count = 0
        self.cell_count = 0

        self.energy_increase_button = Button(self, 'energy_increase', self.settings.screen_width, 100)
        self.energy_reduce_button = Button(self, 'energy_degrease', self.settings.screen_width, 140)
        self.eat_increase_button = Button(self, 'eat_increase', self.settings.screen_width, 180)
        self.eat_reduce_button = Button(self, 'eat_degrease', self.settings.screen_width, 220)

    def run_game(self):
        while True:
            self.birth()
            self.cell_count = 0
            self.kinds_uniq = {}
            self.screen.fill(self.settings.bg_color)

            self.round_counter += 1
            pygame.draw.rect(self.screen, (25, 25, 25), (self.settings.y_start_more_energy, self.settings.y_start_more_energy, self.settings.y_length_more_energy, self.settings.y_length_more_energy))
            pygame.draw.rect(self.screen, (50, 50, 50), (
            self.settings.y_start_anymore_energy, self.settings.y_start_anymore_energy, self.settings.y_length_anymore_energy,
            self.settings.y_length_anymore_energy))


            #pygame.draw.rect(self.screen,[255,255,255], pygame.Rect((1 * self.settings.start_size, 2 * self.settings.start_size, 20, 20)), 5 )


            '''Проход основного цикла жизни с переработкой массива  координат клеток'''
            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell' and self.objects[i][j].action_possibility == True:
                            if self.objects[i][j].kind not in self.kinds_uniq.keys():
                                self.kinds_uniq[self.objects[i][j].kind] = 1
                            else:
                                self.kinds_uniq[self.objects[i][j].kind] += 1
                            actions.life_cycle(self.objects[i][j], self.objects, self.settings)

            """Отрисовка нового масива"""
            for i in range(len((self.objects))):
                for j in range(len(self.objects[i])):
                    if self.objects[i][j] != '0':
                        if self.objects[i][j].type == 'cell':
                            if i != self.objects[i][j].y:
                                print(i, j,  self.objects[i][j].y, self.objects[i][j].x)
                            if j != self.objects[i][j].x:
                                print(j, self.objects[i][j].x, self.objects[i][j])
                            self.cell_count += 1
                            self.objects[i][j].action_possibility = True
                            self.cell_count += 1
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)
                        else:
                            pygame.draw.rect(self.screen, self.objects[i][j].color, self.objects[i][j].object,
                                             self.objects[i][j].line_thin)

            self.event_processing()
            self.energy_increase_button.draw_buttom()
            self.energy_reduce_button.draw_buttom()
            self.eat_increase_button.draw_buttom()
            self.eat_reduce_button.draw_buttom()

            info('Energy coeff: ', self.settings.energy_coef, 10, self.settings.screen_width)
            info('Eat coeff: ', self.settings.eat_coef, 30, self.settings.screen_width)

            pygame.display.flip()

            time.sleep(0.1)
            # self.window.mainloop()


    def birth(self):
        a = random.randint(0, len(self.objects) - 1)
        b = random.randint(0, len(self.objects[0]) - 1)
        if self.objects[a][b] == '0':
            try:
                # self.objects[a][b] = Cell(a, b, random.choice(self.settings.colors), self.genome(), chr(random.randint(65, 91)))
                genome = self.genome()
                self.objects[a][b] = Cell(a, b, actions.color(genome, self.settings), genome, chr(random.randint(65, 91)))
            except IndexError:
                pass

    def genome(self):
        a = []
        a.append('b10')

        while len(a) < self.settings.len_genome:
            a.append(random.choice(('r', 'l', 'b_10',  'c')))


        random.shuffle(a)
        return a

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                y = pos[1] // self.settings.start_size
                x = pos[0] // self.settings.start_size
                if self.energy_increase_button.rect.collidepoint(pos):
                    self.settings.energy_coef += 1
                if self.energy_reduce_button.rect.collidepoint(pos):
                    self.settings.energy_coef -= 1
                if self.eat_increase_button.rect.collidepoint(pos):
                    self.settings.eat_coef += 1
                if self.eat_reduce_button.rect.collidepoint(pos):
                    self.settings.eat_coef -= 1

                # print(pos[1] // self.settings.start_size, pos[0] // self.settings.start_size) отрисовка координат точки куда нажата мышь
                try:
                    print(self.objects[y][x].y, self.objects[y][x].x, self.objects[y][x].kind, self.objects[y][x].color,
                          sorted(self.objects[y][x].genome), self.objects[y][x].energy, self.objects[y][x].life_time)
                except (AttributeError, IndexError):
                    pass

                # get a list of all sprites that are under the mouse cursor
                # clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]
                # do something with the clicked sprites...
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    sorted_tuples = sorted(self.kinds_uniq.items(), key=lambda item: item[1], reverse=True)

                    print(sorted_tuples)
                    counter = 0
                    best_genome = []
                    best_genome_dict = {}
                    for elem in sorted_tuples[:5]:
                        best_genome.append(elem[0])

                    for i in range(len((self.objects))):
                        for j in range(len(self.objects[i])):
                            if self.objects[i][j] != '0':
                                if self.objects[i][j].type == 'cell' and self.objects[i][j].kind in best_genome and \
                                        self.objects[i][j].kind not in best_genome_dict:
                                    best_genome_dict[self.objects[i][j].kind] = (
                                    self.objects[i][j].genome, self.objects[i][j].color)

                    for k, v in best_genome_dict.items():
                        print(k, v[1], sorted(v[0]))

                    print('--------------------------------')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.birth()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.settings.energy_coef += 0.5
                    print(self.settings.energy_coef)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.settings.energy_coef -= 0.5
                    print(self.settings.energy_coef)


if __name__ == "__main__":
    eg = Evolution_game()
    eg.run_game()
