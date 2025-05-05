#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

MOVEMENTS = ['N', 'E', 'S', 'W']

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def move_direction(instruction, x_coord, y_coord, facing):
    '''Execute instruction'''
    global MOVEMENTS
    command = instruction[0]
    total = int(instruction[1:])
    if command == 'W':
        return x_coord - total, y_coord, facing
    elif command == 'E':
        return x_coord + total, y_coord, facing
    elif command == 'N':
        return x_coord, y_coord + total, facing
    elif command == 'S':
        return x_coord, y_coord - total, facing
    elif command == 'F':
        return move_direction(facing + str(total), x_coord, y_coord, facing)
    elif command == 'L':
        steps = int(total/90)
        current_dir = MOVEMENTS.index(facing)
        new_dir = MOVEMENTS[(current_dir - steps) % 4]
        return x_coord, y_coord, new_dir
    elif command == 'R':
        steps = int(total//90)
        current_dir = MOVEMENTS.index(facing)
        new_dir = MOVEMENTS[(current_dir + steps) % 4]
        return x_coord, y_coord, new_dir
    else:
        print("ERROR: wrong input")
        sys.exit(0)


def main():
    directions = get_input('input.txt')

    x_coord = 0
    y_coord = 0
    facing = 'E'

    for direction in directions:
        x_coord, y_coord, facing = move_direction(direction, x_coord, y_coord, facing)

    print(abs(x_coord) + abs(y_coord))


main()
