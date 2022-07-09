import random
import pygame

from My_projects.GAMES.EVOLUTION.actions import settings
from settings import Settings
from cell import Cell

# settings = Settings()


def life_cycle(cell, cell_list, settings):
    """Main circle of events in cells life"""
    settings = settings
    location = nearby_objects(cell, cell_list)
    action = genome_action(cell.genome)

    if action in ('u', 'd', 'r', 'l'):
        square_moving(cell, cell_list, location, action, settings)

    if 'b' in action and cell.energy > settings.start_energy:
        birth(cell, cell_list, action, settings)
        # cell.energy -= int(action[-2:]) * 5
        cell.energy -= cell.energy * 0.5


    if action == 'c':
        collect(cell, settings)

    if "e" in action:
        eat(cell, location, cell_list, action, settings)
        cell.energy -= (cell.genome.count('er') + cell.genome.count('el') + cell.genome.count('ed') + cell.genome.count('eu')) * 3

    energy_reduce(cell, location)

    cell.life_time -= 1
    killer(cell, cell_list, location)


def square_moving(cell, cell_list, location, action, settings):
    if action == 'u' and location[0][1] == '0':
        # print(cell.y, cell.x, action, location[0][1])
        if cell.y > 0:
            cell_list[cell.y - 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y -= 1
        elif cell.y == 0:
            cell_list[cell.y][cell.x] = '0'
            cell_list[settings.y_size][cell.x] = cell
            cell.y = settings.y_size

    if action == 'd' and location[2][1] == '0':
        if cell.y < settings.y_size:
            cell_list[cell.y + 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y += 1
        elif cell.y == settings.y_size:
            cell_list[0][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y = 0

    if action == 'l' and location[1][0] == '0':
        if cell.x > 0:
            cell_list[cell.y][cell.x - 1] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x -= 1
        elif cell.x == 0:
            cell_list[cell.y][cell.x] = '0'
            cell_list[cell.y][cell.settings.x_size] = cell
            cell.x = settings.x_size

    if action == 'r' and location[1][1] == '0':
        if cell.x < settings.x_size:
            cell_list[cell.y][cell.x + 1] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x += 1
        elif cell.x == settings.x_size:
            cell_list[cell.y][0] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x = 0

    cell.object = pygame.Rect((cell.x * cell.width, cell.y * cell.height, cell.width, cell.height))


def collect(cell, settings):
    if settings.y_size - settings.I_y_start_more_energy > cell.y > settings.I_y_start_more_energy and \
            settings.x_size - settings.I_x_start_more_energy > cell.x > settings.I_x_start_more_energy:
        if settings.y_size - settings.I_y_start_anymore_energy > cell.y > settings.I_y_start_anymore_energy and \
                settings.x_size - settings.I_x_start_anymore_energy > cell.x > settings.I_x_start_anymore_energy:
            cell.energy += 0.25 * settings.energy_coef

        cell.energy += 0.75 * settings.energy_coef
    else:
        cell.energy += 0.5 * settings.energy_coef


def nearby_objects(cell, cell_list):
    top = ['-', '0', '-']
    middle = ['0', '0']
    bottom = ['-', '0', '-']

    # top[0] = try_to_see(cell_list, cell.y - 1, cell.x - 1)
    top[1] = try_to_see(cell_list, cell.y - 1, cell.x, settings)
    # top[2] = try_to_see(cell_list, cell.y - 1, cell.x + 1)
    middle[0] = try_to_see(cell_list, cell.y, cell.x - 1, settings)
    middle[1] = try_to_see(cell_list, cell.y, cell.x + 1, settings)
    # bottom[0] = try_to_see(cell_list, cell.y + 1, cell.x - 1)
    bottom[1] = try_to_see(cell_list, cell.y + 1, cell.x, settings)
    # bottom[2] = try_to_see(cell_list, cell.y + 1, cell.x + 1)
    return [top, middle, bottom]


def try_to_see(cell_list, original_y, original_x, settings):
    try:
        a = cell_list[original_y][original_x]
        return a
    except IndexError:
        y = original_y
        x = original_x
        if y > settings.y_size:
            y = 0
        if y < 0:
            y = settings.y_size
        if x > settings.x_size:
            x = 0
        if x < 0:
            x = settings.x_size

        return cell_list[y][x]


def birth(cell, cell_list, action, settings):
    '''Надо помнить, что мутирует ячейка только вврех, ввиду того что при мутации координата указана как у - 1'''

    if settings.y_size > cell.y > 0:
        new_genome = cell.genome.copy()
        random.shuffle(new_genome)
        y = cell.y
        cell_n = Cell(y - 1, cell.x, cell.color, new_genome, cell.kind, cell.energy * 0.5)

        if random.randint(1, 20) == 20:
            genome, kind = mutation(cell.genome, cell.kind)
            cell_n = Cell(y - 1, cell.x, color(genome, settings), genome, kind, cell.energy * 0.5)  # random.choice(settings.colors)

            try:
                if cell_list[y - 1][cell.x] == '0':
                    cell_list[y - 1][cell.x] = cell_n
            except IndexError:
                if cell_list[settings.y_size][cell.x] == '0':
                    cell_list[settings.y_size][cell.x] = cell_n
        else:
            try:
                if cell_list[y - 1][cell.x] == '0':
                    cell_list[y - 1][cell.x] = cell_n
            except IndexError:
                if cell_list[settings.y_size][cell.x] == '0':
                    cell_list[settings.y_size][cell.x] = cell_n


def energy_reduce(cell, location):
    # energy_reduce = 0  # 0 default
    # for raw in location:
    #     energy_reduce += raw.count('-') + raw.count('0')
    # cell.energy -= 1 + (8 - energy_reduce) + round(cell.energy * 0.01)
    cell.energy -= 1 + round(cell.energy * 0.01)


def killer(cell, cell_list, location):
    if cell.energy <= 0 or cell.life_time <= 0:
        # or ("b10" not in cell.genome and "b20" not in cell.genome and "b30" not in cell.genome):
        cell_list[cell.y][cell.x] = '0'


def genome_action(genome):
    action = genome.pop(0)
    genome.append(action)
    return action


def mutation(genome, kind):
    new_gen = random.choice(
        ('b10', 'b20', 'b30', 'b40', 'b50', 'u', 'd', 'l', 'r', 'c', 'el', 'er', 'el', 'ed'))
    new_genome = genome.copy()

    new_genome.pop(random.randint(0, len(new_genome) - 1))
    new_genome.append(new_gen)

    '''Добавить добавление рождаемости при его отсутсвтии'''
    kind_new = kind[:4] + chr(random.randint(65, 90)) + str(random.randint(0, 100))
    return new_genome, kind_new


def eat(cell, location, cell_list, action, settings):
    if action[-1] == 'l' and location[1][0] != '0':
        if location[1][0].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y][cell.x - 1].energy * settings.eat_coef
                cell_list[cell.y][cell.x - 1] = '0'

            except IndexError:
                pass

    if action[-1] == 'r' and location[1][1] != '0':
        if location[1][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y][cell.x + 1].energy * settings.eat_coef
                cell_list[cell.y][cell.x + 1] = '0'

            except IndexError:
                pass

    if action[-1] == 'u' and location[0][1] != '0':
        if location[0][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y - 1][cell.x].energy * settings.eat_coef
                cell_list[cell.y - 1][cell.x] = '0'

            except IndexError:
                pass

    if action[-1] == 'd' and location[2][1] != '0':
        if location[2][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y + 1][cell.x].energy * settings.eat_coef
                cell_list[cell.y + 1][cell.x] = '0'

            except IndexError:
                pass


def color(genome, settings):
    colozing_count = genome.count('c') + genome.count('er') + genome.count('el') + genome.count('ed') +\
                     genome.count('eu') + genome.count('b10') + genome.count('b20') + genome.count('b30') + \
                     genome.count('b40') + genome.count('b50')
    if colozing_count == 0:
        colozing_count = 1
    collect = (255 // colozing_count) * genome.count('c')
    eat = (255 // colozing_count) * (genome.count('er') + genome.count('el') + genome.count('ed')
                                          + genome.count('eu'))
    birth = (255 // colozing_count) * (genome.count('b10') + genome.count('b20') + genome.count('b30') +
                                       genome.count('b40') + genome.count('b50'))
    if eat > 255:
        eat = 255
    if collect > 255:
        collect = 255
    if birth > 255:
        birth = 255

    return [0 + eat, 0 + collect, 0 + birth]
