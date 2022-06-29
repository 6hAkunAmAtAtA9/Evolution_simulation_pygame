import random as random

command = ''


def random_cell():
    r_coeff = random.random()
    if r_coeff > 0.9:
        return 'T'
    elif r_coeff > 0.8:
        return 'R'
    else:
        return '-'


field = [[random_cell() for _ in range(9)] for _ in range(9)]


def show_field(field):
    field[4][4] = 'H'
    for raw in field:
        print(raw)
    pass


def up(field):
    new_raw = [[random_cell() for _ in range(9)]]
    new_raw.extend(field[:8])
    new_raw[5][4] = '-'
    return new_raw


def down(field):
    del field[0]
    field.append([random_cell() for _ in range(9)])
    field[3][4] = ''
    return field


while command != 'q':
    show_field(field)
    command = input('Input a command: ')
    if command == 'w':
        field = up(field)
    elif command == 's':
        field = down(field)
