import random
import pygame
from settings import Settings
from cell import Cell

settings = Settings()


def life_cicle(cell, cell_list):
    """Main circle of events in cells life"""
    print(cell.x, cell.y, cell.genome)
    location = nearby_objects(cell, cell_list)
    if killer(cell, cell_list, location):  # если ложь клетка умерла, смысла жить нет
        potention = get_activities(cell)
        # print('potention', potention)
        if potention >= 90:
            square_moving(cell, cell_list, location)
        if potention > 95:
            birth(cell, cell_list)

        if potention > 100:
            mutation(cell)

        cell.action_possibility = False
        cell.energy -= 1 + cell.genome["Желание_жить"] * 0.3

def square_moving(cell, cell_list, location):
    cell.moving_indicator = random.choice(('up', 'down', 'left', 'right', 'down', 'right', 'left'))  # 2 down added

    if cell.moving_indicator == 'up' and location[0][1] == '0':
        if cell.y - 1 >= 0:
            cell_list[cell.y - 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y -= 1
        else:
            cell_list[settings.y_size][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y = settings.y_size

    if cell.moving_indicator == 'down' and location[2][1] == '0':
        try:
            cell_list[cell.y + 1][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y += 1
        except IndexError:
            cell_list[0][cell.x] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.y = 0

    if cell.moving_indicator == 'left' and location[1][0] == '0':
        if cell.x - 1 >= 0:
            cell_list[cell.y][cell.x - 1] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x -= 1
        else:
            cell_list[cell.y][cell.settings.x_size] = cell
            cell_list[cell.y][cell.x] = '0'
            cell.x = settings.x_size

    if cell.moving_indicator == 'right' and location[1][2] == '0':
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


def birth(cell, cell_list):
    if settings.y_size > cell.y > 0:
        if cell_list[cell.y - 1][cell.x] == '0':
            try:
                cell_list[cell.y - 1][cell.x] = Cell(cell.y - 1, cell.x, cell.color, cell.genome)
            except IndexError:
                pass
        elif cell_list[cell.y + 1][cell.x] == '0':
            try:
                cell_list[cell.y + 1][cell.x] = Cell(cell.y + 1, cell.x, cell.color, cell.genome)
            except IndexError:
                pass


def killer(cell, cell_list, location):
    free_place = 0
    for raw in location:
        free_place += raw.count('0') + raw.count('-')
    if cell.energy <= 0 or free_place < settings.free_place_needing:
        cell_list[cell.y][cell.x] = '0'
        return False
    return True


def get_activities(cell):
    potention = random.randint(0, 100) + cell.genome['Желание_жить']

    return potention


def mutation(cell):
    if cell.genome['Желание_жить'] < 50:
        cell.genome['Желание_жить'] = round(cell.genome['Желание_жить'] + 0.1, 1)
        if 255 > cell.color[0] > 0:
            cell.color[0] -= 1
        elif 255 > cell.color[0] > 0:
            cell.color[1] -= 1
        elif 255 > cell.color[0] > 0:
            cell.color[2] -= 1
        else:
            pass
