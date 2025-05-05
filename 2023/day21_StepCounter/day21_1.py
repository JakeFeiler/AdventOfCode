#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    garden = get_input('input.txt')

    length, height = len(garden[0]), len(garden)
    for row_pos, row in enumerate(garden):
        for col_pos, plot  in enumerate(row):
            if plot == 'S':
                start_y, start_x = row_pos, col_pos
                break

    current_spaces_reached = set([(start_y, start_x)])
    for steps in range(64):
        next_spaces = set()
        for current_plot in current_spaces_reached:
            (y_coord, x_coord) = current_plot
            if x_coord > 0 and garden[y_coord][x_coord - 1] != '#':
                next_spaces.add((y_coord, x_coord - 1))
            if y_coord > 0 and garden[y_coord - 1][x_coord] != '#':
                next_spaces.add((y_coord - 1, x_coord))
            if x_coord < length - 1 and garden[y_coord][x_coord + 1] != '#':
                next_spaces.add((y_coord, x_coord + 1))
            if y_coord < height - 1 and garden[y_coord + 1][x_coord] != '#':
                next_spaces.add((y_coord + 1, x_coord))
        current_spaces_reached = next_spaces

    print(len(current_spaces_reached))



main()
