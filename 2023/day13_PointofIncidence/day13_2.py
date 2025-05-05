#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import numpy as np
import math
import pdb

#>31703

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def possible_mirror(val1, val2):
    '''Determine if these 2 values could be reflections, off by a 1'''
    #The difference in the values will be a single 1 vs 0, which is a power of 10, so check the log for a whole number
    #However, need to check within a very loose range to ensure no rounding error
    diff = abs(val1-val2)

    #diff = 0 - perfect reflection 
    if diff == 0:
        return False
    power_of_ten = math.log(diff, 10)


    margin_of_error = 1e-14
    rounded_value = round(power_of_ten)
    #if val1 == 101111010000110 and val2 == 101110010000110:    
    #    print(power_of_ten, rounded_value - power_of_ten, abs(rounded_value - power_of_ten) < margin_of_error)     
    return (abs(rounded_value - power_of_ten)) < margin_of_error

def find_mirror(valley):
    '''Determine the location of the mirror in the valley'''

    row_values = []
    #Dictionary of rows for every value
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
        smudge_count = 0
        #Looking for consecutive matching rows
        is_possible_mirror = possible_mirror(value, prev_row_value)
        if prev_row_value != value and not is_possible_mirror:
            prev_row_value = value
        else:
            if row_pos <= len(row_values)/2:
                max_dist_to_look = row_pos
            else:
                max_dist_to_look = len(row_values) - row_pos

            if is_possible_mirror:
                smudge_count += 1

            for a in range(2,max_dist_to_look + 1):
                if possible_mirror(row_values[row_pos - a],  row_values[row_pos + a - 1]):
                    smudge_count += 1

                elif row_values[row_pos - a] != row_values[row_pos + a - 1]:
                    smudge_count = 10
                    break

            #Need exactly 1 smudge
            if smudge_count == 1:
                return 100*row_pos
            prev_row_value = value

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
