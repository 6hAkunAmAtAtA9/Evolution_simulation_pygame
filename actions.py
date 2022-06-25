import random
import pygame
from settings import Settings
from cell import Cell

settings = Settings()


def life_cicle(cell, cell_list):
    """Main circle of events in cells life"""
    location = nearby_objects(cell, cell_list)
    action = genome_action(cell.genome)

    if action in ('u', 'd', 'r', 'l'):
        square_moving(cell, cell_list, location, action)
        cell.disabled_counter = settings.disabled_counter
    if 'b' in action and cell.energy > int(action[-2:]) * 4:
        birth(cell, cell_list, action)
        cell.energy -= int(action[-2:]) * 4

    if action == 'c':
        collect(cell)

    if "e" in action:
        eat(cell, location, cell_list, action)
        cell.energy -= 10

    energy_reduce(cell, location)
    killer(cell, cell_list, location)


def square_moving(cell, cell_list, location, action):
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

def collect(cell):
    if settings.y_size - settings.I_y_start_more_energy > cell.y > settings.I_y_start_more_energy and \
            settings.x_size - settings.I_x_start_more_energy > cell.x > settings.I_x_start_more_energy:
        if settings.y_size - settings.I_y_start_anymore_energy > cell.y > settings.I_y_start_anymore_energy and \
                settings.x_size - settings.I_x_start_anymore_energy > cell.x > settings.I_x_start_anymore_energy:
            cell.energy += 7

        cell.energy += 3
    else:
        cell.energy += 1

def nearby_objects(cell, cell_list):
    top = ['-', '0', '-']
    middle = ['0', '0']
    bottom = ['-', '0', '-']

    # top[0] = try_to_see(cell_list, cell.y - 1, cell.x - 1)
    top[1] = try_to_see(cell_list, cell.y - 1, cell.x)
    # top[2] = try_to_see(cell_list, cell.y - 1, cell.x + 1)
    middle[0] = try_to_see(cell_list, cell.y, cell.x - 1)
    middle[1] = try_to_see(cell_list, cell.y, cell.x + 1)
    # bottom[0] = try_to_see(cell_list, cell.y + 1, cell.x - 1)
    bottom[1] = try_to_see(cell_list, cell.y + 1, cell.x)
    # bottom[2] = try_to_see(cell_list, cell.y + 1, cell.x + 1)
    return [top, middle, bottom]

def try_to_see(cell_list, original_y, original_x):
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

def birth(cell, cell_list, action):
    '''Надо помнить, что мутирует ячейка только вврех, ввиду того что при мутации координата указана как у - 1'''
    if settings.y_size > cell.y > 0:
        new_genome = cell.genome.copy()
        random.shuffle(new_genome)
        y = cell.y
        cell_n = Cell(y - 1, cell.x, cell.color, new_genome, cell.kind, action[-2:])

        if random.randint(1, 20) == 20:
            genome, kind = mutation(cell.genome, cell.kind)
            cell_n = Cell(y - 1, cell.x, random.choice(settings.colors), genome, kind, action[-2:])

        if cell_list[y - 1][cell.x] == '0':
            try:
                cell_list[y - 1][cell.x] = cell_n
            except IndexError:
                pass

        elif cell_list[cell.y + 1][cell.x] == '0':
            try:

                cell_list[cell.y + 1][cell.x] = Cell(y + 1, cell.x, cell.color, new_genome, cell.kind, action[-2:])
            except IndexError:
                pass

def energy_reduce(cell, location):
    energy_reduce = 0
    for raw in location:
        energy_reduce += raw.count('-') + raw.count('0')
    cell.energy -= 1 + (8 - energy_reduce) + round(cell.energy * 0.01)

def killer(cell, cell_list, location):
    if cell.energy <= 0:
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

def eat(cell, location, cell_list, action):
    if action[-1] == 'l' and location[1][0] != '0':
        if location[1][0].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y][cell.x - 1].energy * 2
                cell_list[cell.y][cell.x - 1] = '0'

            except IndexError:
                pass

    if action[-1] == 'r' and location[1][1] != '0':
        if location[1][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y][cell.x + 1].energy * 2
                cell_list[cell.y][cell.x + 1] = '0'

            except IndexError:
                pass

    if action[-1] == 'u' and location[0][1] != '0':
        if location[0][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y - 1][cell.x].energy * 2
                cell_list[cell.y - 1][cell.x] = '0'

            except IndexError:
                pass

    if action[-1] == 'd' and location[2][1] != '0':
        if location[2][1].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y + 1][cell.x].energy * 2
                cell_list[cell.y + 1][cell.x] = '0'

            except IndexError:
                pass
