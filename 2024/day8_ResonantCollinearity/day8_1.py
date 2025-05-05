#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd
import itertools

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    height = len(s)
    width = len(s[0])
    node_locations = dd(list)
    antinode_locations = set()
    for row_pos, row in enumerate(s):
        for col_pos, value in enumerate(row):
            if value != '.':
                node_locations[value].append((col_pos, row_pos))
    for unique_node in node_locations:
        #For the same value, take every possible pair of nodes
        node_pairs = itertools.combinations(node_locations[unique_node], 2)
        for pair in node_pairs:
            #Calculate difference in distance, determine antinode position
            x_0, y_0, x_1, y_1 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
            x_diff = x_0 - x_1
            y_diff = y_0 - y_1
            antinode_1 = (x_0 + x_diff, y_0 + y_diff)
            antinode_2 = (x_1 - x_diff, y_1 - y_diff)
            if 0 <= antinode_1[0] < width and 0 <= antinode_1[1] < height:
                antinode_locations.add(antinode_1)
            if 0 <= antinode_2[0] < width and 0 <= antinode_2[1] < height:
                antinode_locations.add(antinode_2)

    print(len(antinode_locations))



main()
