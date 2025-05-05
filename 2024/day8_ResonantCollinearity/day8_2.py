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

            #Traverse in both directions until we hit edge of map
            antinode_x, antinode_y = x_0, y_0
            while 0 <= antinode_x < width and 0 <= antinode_y < height:
                antinode_locations.add((antinode_x, antinode_y))
                antinode_x += x_diff
                antinode_y += y_diff

            antinode_x, antinode_y = x_1, y_1
            while 0 <= antinode_x < width and 0 <= antinode_y < height:
                antinode_locations.add((antinode_x, antinode_y))
                antinode_x -= x_diff
                antinode_y -= y_diff

    print(len(antinode_locations))



main()
