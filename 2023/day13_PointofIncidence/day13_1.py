#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_mirror(valley):
    '''Determine the location of the mirror in the valley'''


    row_values = []
    #Turn row into integer made of 1's and 0's (not binary)
    for lscape_row in valley:
        row_value = 0
        for lscape in lscape_row:
            if lscape == '#':
                row_value = row_value*10 + 1
            else:
                row_value *= 10
        row_values.append(row_value)
        row_value = 0

    prev_row_value = -1
    for row_pos, value in enumerate(row_values):
        #Looking for consecutive matching rows
        if value != prev_row_value:
            prev_row_value = value
        else:
            if row_pos <= len(row_values)/2:
                max_dist_to_look = row_pos
            else:
                max_dist_to_look = len(row_values) - row_pos
                
            is_matching = True
            for a in range(2,max_dist_to_look + 1):
                if row_values[row_pos - a] != row_values[row_pos + a - 1]:
                    is_matching = False
                    break
            if is_matching:
                return 100*row_pos

    #Couldn't find a row reflection - try a column reflection
    return int(.01*find_mirror(valley.T))

def main():
    s = get_input('input.txt')

    valley = []
    final_value = 0
    for row in s:
        if row != '':
            valley.append(list(row))
        else:
            valley_matrix = np.array(valley)
            final_value += find_mirror(valley_matrix)
            valley = []

    final_value += find_mirror(np.array(valley))
    print(final_value)



main()
