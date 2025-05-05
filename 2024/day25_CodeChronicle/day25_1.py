#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math
import numpy as np

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    #Inspection - schematics are 7 high
    #N schematics, N-1 lines -> divide by 8, ceiiling
    keys = []
    locks = []
    schematic_count = math.ceil(len(s)/8)
    for sc_count in range(schematic_count):
        schema = s[sc_count*8:sc_count*8+8]
        #Count number of filled spaces in each column
        pattern = [0]*5
        for row in schema:
            for col_pos,col in enumerate(row):
                if col == '#':
                    pattern[col_pos] += 1
        if '.' in schema[0]:
            keys.append(pattern)
        else:
            locks.append(pattern)

    keys = list(map(np.array, keys))
    locks = list(map(np.array, locks))
    fits = 0
    for key in keys:
        for lock in locks:
            fit = key + lock
            #Key/lock fit will have fewer than 7 pips in any column
            if max(fit) <= 7:
                fits += 1
    print(fits)

main()
