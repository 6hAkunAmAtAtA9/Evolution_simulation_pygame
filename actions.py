import random
import pygame
from settings import Settings
settings = Settings()


def life_cicle(cell, cell_list):
    """Main circle of events in cells life"""
    location = nearby_objects(cell, cell_list)

    square_moving(cell, cell_list, location)
    #print(location[0], location[1], location[2], sep='\n')
    #print("**************")
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

    if cell.moving_indicator == 'up' and cell.y >= cell.height and location[0][1] == '0':
        cell.y -= cell.height
        cell.energy -= 1

    if cell.moving_indicator == 'down' and cell.y <= settings.screen_height - 2 * cell.height and location[2][1] == '0':
        cell.y += cell.height
        cell.energy -= 1

    if cell.moving_indicator == 'right' and cell.x >= cell.width and location[1][0] == '0':
        cell.x -= cell.width
        cell.energy -= 1

    if cell.moving_indicator == 'left' and cell.x <= settings.screen_width - 2 * cell.width and location[1][2] == '0':
        cell.x += cell.width
        cell.energy -= 1

    cell.object = pygame.Rect((cell.x, cell.y, cell.width, cell.height))

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
    for k, v in cell_list.items():
        if cell == v:
            continue
        if v.x - cell.width <= cell.x <= v.x + cell.width:
            if v.y - cell.height <= cell.y <= v.y + cell.height:
                if v.x - cell.width == cell.x:
                    if v.y + cell.height == cell.y:
                        top[2] = [k, v.type[0]]
                    elif v.y == cell.y:
                        middle[2] = [k, v.type[0]]
                    else:
                        bottom[2] = [k, v.type[0]]
                elif v.x == cell.x:
                    if v.y + cell.height == cell.y:
                        top[1] = [k, v.type[0]]
                    else:
                        bottom[1] = [k, v.type[0]]
                else:
                    if v.y + cell.height == cell.y:
                        top[0] = [k, v.type[0]]
                    elif v.y == cell.y:
                        middle[0] = [k, v.type[0]]
                    else:
                        bottom[0] = [k, v.type[0]]
    return [top, middle, bottom]

def killer(cell_list:dict):
    kill_list = []
    for k, v in cell_list.items():
        if v.energy <= 0:
            kill_list.append(k)

    [cell_list.pop(key) for key in kill_list]




