#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np
import time

#<118784

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def shift_rocks(platform):
    '''Slide the rocks right to left'''
    new_platform = [['.' for _ in range(len(platform[0]))] for _ in range(len(platform))]
    for row_pos, row in enumerate(platform):
        target_loc = 0
        for col_pos, spot in enumerate(row):
            if spot == 'O':
                new_platform[row_pos][target_loc] = 'O'
                target_loc += 1
            elif spot == '#':
                new_platform[row_pos][col_pos] = '#'
                target_loc = col_pos + 1


    return np.array(new_platform)

def spin_cycle(platform):
    '''Run spin cycle 1000000000 times'''
    spin_count = 1_000_000_000
    found_patterns = {}

    spin = 0
    while spin < spin_count:
        spin += 1

        platform_after_n = shift_rocks(np.rot90(platform))
        platform_after_w = shift_rocks(np.rot90(platform_after_n, k = 3))
        platform_after_s = shift_rocks(np.rot90(platform_after_w, k = 3))
        platform_after_e = shift_rocks(np.rot90(platform_after_s, k = 3))
        platform = np.rot90(platform_after_e, k = 2)



        hashable_string = "".join(["".join(row) for row in platform])
        hashed_platform = hash(hashable_string)
        try:
            last_time = found_patterns[hashed_platform]
            found_patterns = {}         
            remaining_cycles = spin_count // (spin - last_time)
            spin += (spin - last_time) * (remaining_cycles - 2)
        except:
            found_patterns[hashed_platform] = spin


    return platform

def find_total_load(platform_matrix):
    '''Compute the load when tilted North'''
    #Easier to work with rows - transpose the matrix
    platform_matrix = np.rot90(platform_matrix, k = 3)
    total_load = 0

    for row in platform_matrix:
        for spot_pos, spot in enumerate(row):
            if spot == 'O':
                total_load += spot_pos + 1

    return total_load

def main():
    s = get_input('input.txt')
    platform = []
    for row in s:
        platform.append(list(row))

    cycled_platform = spin_cycle(platform)
    platform_matrix = np.array(cycled_platform)
    total_load = find_total_load(platform_matrix)
    print(total_load)


main()
