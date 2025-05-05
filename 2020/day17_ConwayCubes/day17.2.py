#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np
import time

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def boot_up_cube(cube, cycles):
    '''Conway's Game of Life on cube for <cycles> steps'''
    while cycles > 0:
        cycles -= 1
        cube_copy = np.copy(cube)
        for coords, val in np.ndenumerate(cube_copy):
            w, z, y, x = coords[0], coords[1], coords[2], coords[3]
            #Get all indexes of neighboring cells
            neighbor_coords = []
            for w_neighbor in list(range(-1, 2)):
                for z_neighbor in list(range(-1, 2)):
                    for y_neighbor in list(range(-1, 2)):
                        for x_neighbor in list(range(-1, 2)):
                            if (w_neighbor != 0 or z_neighbor != 0 or y_neighbor != 0 or x_neighbor != 0):
                                neighbor_coords.append((w  + w_neighbor, z + z_neighbor, y + y_neighbor, x + x_neighbor))
            #Sum all values of neighboring cells
            neighbor_sum = 0
            for neighbor in neighbor_coords:
                try:
                    neighbor_sum += cube_copy[neighbor[0], neighbor[1], neighbor[2], neighbor[3]]
                except:
                    pass
            #Update Cube
            if (val == 0 and neighbor_sum == 3) or (val == 1 and neighbor_sum in [2, 3]):
                cube[w][z][y][x] = 1
            else:
                cube[w][z][y][x] = 0

    return cube



def main():
    #VERY INEFFICIENT: ~25 SECONDS TO RUN
    #start = time.time()
    np.set_printoptions(threshold=sys.maxsize)
    s = get_input('input.txt')

    cycles_to_run = 6
    max_x_dimension = len(s[0]) + cycles_to_run * 2
    max_y_dimension = len(s) + cycles_to_run * 2
    max_z_dimension = 1 + 2 * cycles_to_run
    max_w_dimension = 1 + 2 * cycles_to_run

    cube = np.zeros((max_w_dimension, max_z_dimension, max_y_dimension, max_x_dimension))

    for row_num, row in enumerate(s):
        for col_num, col in enumerate(row):
            if col == '#':
                w = cycles_to_run
                z = cycles_to_run
                y = cycles_to_run + row_num
                x = cycles_to_run + col_num
                cube[w][z][y][x] = 1


    final_cube = boot_up_cube(cube, cycles_to_run)
    print(int(np.sum(np.concatenate(final_cube))))


    #execution_time = (time.time() - start)
    #print('Execution time in seconds: ' + str(execution_time))


main()
