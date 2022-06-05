import random
import pygame
from settings import Settings
from cell import Cell

settings = Settings()


def life_cicle(cell, cell_list, b_k, m_k, d_k):
    """Main circle of events in cells life"""
    # print(cell.x, cell.y, cell.genome)

    location = nearby_objects(cell, cell_list)
    action = genome_action(cell.genome)
    # print(cell.x, cell.y)
    # print(location[0])
    # print(location[1])
    # print(location[2])


    if action in ('u', 'd', 'r', 'l'):
        square_moving(cell, cell_list, location, action)
    if 'b' in action and cell.energy > int(action[-2:]):
        birth(cell, cell_list, action, m_k)
        cell.energy -= int(action[-2:])

    if action == 'c':
        cell.energy += 10

    if "e" in action:
        eat(cell, location, cell_list, action)
        cell.energy -= 10

    cell.action_possibility = False
    cell.energy -= 1

    killer(cell, cell_list, location, d_k)



def square_moving(cell, cell_list, location, action):
    if action == 'u' and location[0][1] == '0':

        if cell.y - 1 >= 0:
            cell_list[cell.y - 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y -= 1
        else:
            cell_list[settings.y_size][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y = settings.y_size

    if action == 'd' and location[2][1] == '0':
        try:
            cell_list[cell.y + 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y += 1
        except IndexError:
            cell_list[0][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y = 0

    if action == 'l' and location[1][0] == '0':
        if cell.x - 1 >= 0:
            cell_list[cell.y][cell.x - 1] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x -= 1
        else:
            cell_list[cell.y][cell.settings.x_size] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x = settings.x_size

    if action == 'r' and location[1][2] == '0':
        try:
            cell_list[cell.y][cell.x + 1] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x += 1
        except IndexError:
            cell_list[cell.y][0] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x = 0

    cell.object = pygame.Rect((cell.x * cell.width, cell.y * cell.height, cell.width, cell.height))


def nearby_objects(cell, cell_list):
    top = ['-', '0', '-']
    middle = ['0', 'C', '0']
    bottom = ['-', '0', '-']

    # top[0] = try_to_see(cell_list, cell.y - 1, cell.x - 1)
    top[1] = try_to_see(cell_list, cell.y - 1, cell.x)
    # top[2] = try_to_see(cell_list, cell.y - 1, cell.x + 1)
    middle[0] = try_to_see(cell_list, cell.y, cell.x - 1)
    middle[2] = try_to_see(cell_list, cell.y, cell.x + 1)
    # bottom[0] = try_to_see(cell_list, cell.y + 1, cell.x - 1)
    bottom[1] = try_to_see(cell_list, cell.y + 1, cell.x)
    # bottom[2] = try_to_see(cell_list, cell.y + 1, cell.x + 1)
    return [top, middle, bottom]


def try_to_see(cell_list, oringinal_y, original_x):
    try:
        a = cell_list[oringinal_y][original_x]
    except IndexError:
        if oringinal_y > settings.y_size:
            a = cell_list[0][original_x]
        if oringinal_y < 0:
            a = cell_list[settings.y_size][original_x]
        if original_x > settings.x_size:
            a = cell_list[oringinal_y][0]
        if original_x < 0:
            a = cell_list[oringinal_y][settings.x_size]
    return a


def birth(cell, cell_list, action, m_k):
    if settings.y_size >= cell.y > 0:
        new_genome = cell.genome.copy()
        random.shuffle(new_genome)

        cell_n = Cell(cell.y - 1, cell.x, cell.color, new_genome, cell.kind, action[-2:])

        if random.randint(1, 50) == 50:
            genome, kind = mutation(cell.genome, cell.kind)
            cell_n = Cell(cell.y - 1, cell.x, random.choice(settings.colors), genome, kind, action[-2:])


        if cell_list[cell.y - 1][cell.x] == '0':
            try:
                cell_list[cell.y - 1][cell.x] = cell_n
            except IndexError:
                pass


def killer(cell, cell_list, location, d_k):
    taken_place = 8
    for raw in location:
        taken_place -= raw.count('0') + raw.count('-')
    if cell.energy <= 0 or taken_place > settings.free_place_needing or (
            "b10" not in cell.genome and "b20" not in cell.genome and "b30" not in cell.genome):
        cell_list[cell.y][cell.x] = '0'



def genome_action(genome):
    action = genome.pop(0)
    genome.append(action)
    return action


def mutation(genome, kind):
    new_gen = random.choice(
        ('b10', 'b20', 'b30', 'b40', 'b50', 'u', 'd', 'l', 'r', 'c', 'el', 'er'))
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
                cell.energy += cell_list[cell.y][cell.x - 1].energy
                cell_list[cell.y][cell.x - 1] = '0'

            except IndexError:
                pass

    if action[-1] == 'r' and location[1][2] != '0':
        if location[1][2].kind != cell.kind:
            try:
                cell.energy += cell_list[cell.y][cell.x + 1].energy
                cell_list[cell.y][cell.x + 1] = '0'

            except IndexError:
                pass