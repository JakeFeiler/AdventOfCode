#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_total_load(platform_matrix):
    '''Compute the load when tilted North'''
    #Easier to work with rows - transpose the matrix
    platform_matrix = np.rot90(platform_matrix)
    total_load = 0

    max_row_load = len(platform_matrix[0])
    for row in platform_matrix:
        current_load = max_row_load
        for pos, spot in enumerate(row):
            if spot == 'O':
                total_load += current_load
                current_load -=1
            if spot == '#':
                current_load = max_row_load - pos - 1

    return total_load

def main():
    s = get_input('input.txt')
    platform = []
    for row in s:
        platform.append(list(row))
    platform_matrix = np.array(platform)
    total_load = find_total_load(platform_matrix)
    print(total_load)


main()
