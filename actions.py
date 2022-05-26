import random
import pygame
from settings import Settings
from cell import Cell
settings = Settings()


def life_cicle(cell, cell_list):
    """Main circle of events in cells life"""
    location = nearby_objects(cell, cell_list)
    birth(cell, cell_list, location)
    square_moving(cell, cell_list, location)
    cell.action_possibility = False
    cell.freedom_love += 1





    #print(location[0], location[1], location[2], sep='\n')
    #print(nearby_objects(cell, cell_list))


# Первое движение(плавное)
def moving(cell):

    if cell.step_counter == 0:
        cell.moving_indicator = random.randint(1, 4)
        cell.moving_leight = random.randint(0, 50)

        if cell.moving_indicator == 1 and cell.x < cell.settings.screen_width - cell.width:
            cell.move_right_flag = True
        elif cell.moving_indicator == 2 and cell.x > 0:
            cell.move_left_flag = True
        elif cell.moving_indicator == 3 and cell.y > 0:
            cell.move_up_flag = True
        elif cell.moving_indicator == 4 and cell.y < cell.settings.screen_height - cell.height:
            cell.move_down_flag = True

    if cell.x >= cell.settings.screen_width - cell.width or cell.step_counter == cell.moving_leight:
        cell.move_right_flag = False
    if cell.x <= 0 or cell.step_counter == cell.moving_leight:
        cell.move_left_flag = False
    if cell.y >= cell.settings.screen_height - cell.height or cell.step_counter == cell.moving_leight:
        cell.move_down_flag = False
    if cell.y <= 0 or cell.step_counter == cell.moving_leight:
        cell.move_up_flag = False

    if cell.step_counter == cell.moving_leight or (not cell.move_right_flag and not cell.move_left_flag
                                                   and not cell.move_up_flag and not cell.move_down_flag):
        cell.step_counter = 0

    if cell.move_right_flag:
        cell.x += 1

        cell.step_counter += 1

    if cell.move_left_flag:
        cell.x -= 1

        cell.step_counter += 1

    if cell.move_up_flag:
        cell.y -= 1

        cell.step_counter += 1

    if cell.move_down_flag:
        cell.y += 1

        cell.step_counter += 1

    cell.object = pygame.Rect((cell.x, cell.y, cell.width, cell.height))

def square_moving(cell, cell_list, location):
    cell.moving_indicator = random.choice(('up', 'down', 'left', 'right'))

    if cell.moving_indicator == 'up' and location[0][1] == '0':
        cell_list[cell.y - 1][cell.x] = cell
        cell_list[cell.y][cell.x] = '0'
        cell.y -= 1
        cell.energy -= 1
        cell.freedom_love -= 2

    if cell.moving_indicator == 'down' and location[2][1] == '0':
        cell_list[cell.y + 1][cell.x] = cell
        cell_list[cell.y][cell.x] = '0'
        cell.y += 1
        cell.energy -= 1
        cell.freedom_love -= 2

    if cell.moving_indicator == 'left' and location[1][0] == '0':
        cell_list[cell.y][cell.x - 1] = cell
        cell_list[cell.y][cell.x] = '0'
        cell.x -= 1
        cell.energy -= 1
        cell.freedom_love -= 2

    if cell.moving_indicator == 'right' and location[1][2] == '0':
        cell_list[cell.y][cell.x + 1] = cell
        cell_list[cell.y][cell.x] = '0'
        cell.x += 1
        cell.energy -= 1
        cell.freedom_love -= 2

    cell.object = pygame.Rect((cell.x * cell.width, cell.y * cell.height, cell.width, cell.height))

def movement_possibility(cell, cell_list):
    for v in cell_list.values():
        if cell == v:
            continue
        if cell.x == v.x and cell.y == v.y:
            return False
    return True

def nearby_objects(cell, cell_list):
    top = ['0', '0', '0']
    middle = ['0', 'C', '0']
    bottom = ['0', '0', '0']

    top[0] = try_to_see(cell_list, cell.y - 1, cell.x - 1)
    top[1] = try_to_see(cell_list, cell.y - 1, cell.x)
    top[2] = try_to_see(cell_list, cell.y - 1, cell.x + 1)
    middle[0] = try_to_see(cell_list, cell.y, cell.x - 1)
    middle[2] = try_to_see(cell_list, cell.y, cell.x + 1)
    bottom[0] = try_to_see(cell_list, cell.y + 1, cell.x - 1)
    bottom[1] = try_to_see(cell_list, cell.y + 1, cell.x)
    bottom[2] = try_to_see(cell_list, cell.y + 1, cell.x + 1)
    return [top, middle, bottom]

def try_to_see(cell_list, oringinal_y, original_x):
    a = '-'
    if original_x < 0 or oringinal_y < 0:
        return '-'
    try:
        a = cell_list[oringinal_y][original_x]
    except IndexError:
        a = '-'
    return a


def birth(cell, cell_list, location):
    birth_probability = random.randint(1, 5)
    if birth_probability >= 5 and len(cell_list) - 1 > cell.y > 1:
        if cell_list[cell.y - 1][cell.x] == '0':
            try:
                cell_list[cell.y - 1][cell.x] = Cell(cell.y - 1, cell.x, cell.color)

            except IndexError:
                pass
        elif cell_list[cell.y + 1][cell.x] == '0':
            try:
                cell_list[cell.y + 1][cell.x] = Cell(cell.y + 1, cell.x, cell.color)
            except IndexError:
                pass



def killer(cell_list, death_count):
    for i in range(len(cell_list)):
        for j in range(len(cell_list[i])):
            if cell_list[i][j] != '0':
                if (cell_list[i][j].type == 'cell' and cell_list[i][j].freedom_love > 10) or cell_list[i][j].energy == 0:
                    cell_list[i][j] = '0'
                    death_count += 1
    return death_count







