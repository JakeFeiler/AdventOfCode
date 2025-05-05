#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def get_cave_size(rock_shapes):
    '''Get the dimensions of the cave'''
    max_cols = 0
    max_rows = 0
    for path in rock_shapes:
        endpoints = path.split(' -> ')
        for endpoint in endpoints:
            endpoint = endpoint.split(',')
            max_cols = max(max_cols, int(endpoint[0]))
            max_rows = max(max_rows, int(endpoint[1]))
    #1 extra 500 column to (hopefully) allow sand to rach
    #3 Extra columns
    #Ex: If max y = 9:
    #Need 10 total rows to graph this
    #And 2 more per spec
    return max_cols + 500, max_rows + 3

def chart_cave(rock_shapes, rows, cols):
    '''Create a map of the cave'''
    cave_shape = [['.' for r in range(cols)] for c in range(rows)]
    #first coord is going down, 2nd coord is going across
    for path in rock_shapes:
        endpoints = path.split(' -> ')
        #for every corner on a path, trace the path to the next turn
        for index, endpoint in enumerate(endpoints[:-1]):
            x, y = map(int, endpoint.split(','))
            next_x, next_y = map(int, endpoints[index + 1].split(','))
            cave_shape[y][x] = '#'
            if x == next_x:
                if y < next_y:
                    while y < next_y:
                        y += 1
                        cave_shape[y][x] = '#'
                else:
                    while y > next_y:
                        y -= 1
                        cave_shape[y][x] = '#'
            else:
                if x < next_x:
                    while x < next_x:
                        x += 1
                        cave_shape[y][x] = '#'
                else:
                    while x > next_x:
                        x -= 1
                        cave_shape[y][x] = '#'

    #Fill bottom
    for column in range(len(cave_shape[-1])):
        cave_shape[rows - 1][column] = '#'

    return cave_shape

def main():
    s = get_input('input.txt')

    max_cols, max_rows = get_cave_size(s)
    cave = chart_cave(s, max_rows, max_cols)

    fallen_sand = 0
    while True:
        grain_coords = (500, 0)
        can_fall = True
        while can_fall:
            x, y = grain_coords[0], grain_coords[1]
            if cave[y + 1][x] == '.':
                grain_coords = (x, y + 1)
            elif cave[y + 1][x - 1] == '.':
                grain_coords = (x - 1, y + 1)
            elif cave[y + 1][x + 1] == '.':
                grain_coords = (x + 1, y + 1)
            else:
                can_fall = False
                cave[y][x] = '#'
                fallen_sand += 1
                if (x, y) == (500, 0):
                    print(fallen_sand)
                    sys.exit(0)

main()
