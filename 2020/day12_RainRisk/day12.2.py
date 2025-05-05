#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
 
def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def move_direction(instruction, x_coord, y_coord, wp_x, wp_y):
    '''Execute instruction'''
    global MOVEMENTS
    command = instruction[0]
    total = int(instruction[1:])
    if command == 'W':
        return x_coord, y_coord, wp_x - total, wp_y
    elif command == 'E':
        return x_coord, y_coord, wp_x + total, wp_y
    elif command == 'N':
        return x_coord, y_coord, wp_x, wp_y + total
    elif command == 'S':
        return x_coord, y_coord, wp_x, wp_y - total
    elif command == 'F':
        return x_coord + wp_x*total, y_coord + wp_y*total, wp_x, wp_y
    elif command == 'L':
        steps = int(total/90)
        for step in range(steps):
            wp_x, wp_y = -wp_y, wp_x
        return x_coord, y_coord, wp_x, wp_y
    elif command == 'R':
        steps = int(total/90)
        for step in range(steps):
            wp_x, wp_y = wp_y, -wp_x
        return x_coord, y_coord, wp_x, wp_y
    else:
        print("ERROR: wrong input")
        sys.exit(0)


def main():
    directions = get_input('input.txt')

    x_coord = 0
    y_coord = 0
    wp_x = 10
    wp_y = 1

    for direction in directions:
        x_coord, y_coord, wp_x, wp_y = move_direction(direction, x_coord, y_coord, wp_x, wp_y)

    print(abs(x_coord) + abs(y_coord))


main()
