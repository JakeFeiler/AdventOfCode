#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from copy import deepcopy

MAZE = {}

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def prune_maze(height, width):
    '''Any dot touching 3 #'s is a dead end -> turn it into a #'''
    #E & S border 2 paths, no worries there
    global MAZE
    pruning_to_do = True
    while pruning_to_do:
        pruning_to_do = False
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                borders = [MAZE[x + 1 + 1j*y], MAZE[x - 1 + 1j*y], MAZE[x + 1j*(y + 1)], MAZE[x + 1j*(y - 1)]]
                current_marking = MAZE[x + 1j*y]
                if borders.count('#') == 3 and current_marking == '.':
                    MAZE[x + 1j*y] = '#'
                    pruning_to_do = True
    return MAZE

def find_score(start, end, direction):
    """Find the best score using djikstra's"""
    quickest_paths = {}
    global MAZE
    #Maintain a quickest path of the tuple of (coord, direction)
    #Could be a bit more optimized, but shouldn't be too impacful

    #Would use a heap, but seems tricky with tuples. We'll stick to array for now.
    #Tuple: Position, direction, score
    next_squares_to_explore = [(start, direction, 0)]

    while True:
        next_square = min(next_squares_to_explore, key=lambda x: x[2])
        next_squares_to_explore.remove(next_square)
        coords, direction, score = next_square[0], next_square[1], next_square[2]
        #Check if this is the end
        if coords == end:
            return score
            #return score
        for next_dir in [direction, direction*1j, direction*-1j]:
            next_coord = coords + next_dir
            #Not a wall
            if MAZE[next_coord] != '#':
                #Hasn't been visited yet - update quickest path, and explore it later
                #if (next_coord, next_dir) not in quickest_paths:
                next_score = score + 1
                if next_dir != direction:
                    next_score += 1000
                #In theory, shouldn't have needed the 2nd check as djikstra would avoid it, but something slipped up i.e. visited a square where improvement could be made -> perhaps a turn?
                if (next_coord, next_dir) not in quickest_paths or quickest_paths[(next_coord, next_dir)] > next_score:
                    quickest_paths[(next_coord, next_dir)] = next_score
                    next_squares_to_explore.append((next_coord, next_dir, next_score))


def main():
    s = get_input('input.txt')
    direction = 1
    start = 0
    end = 0

    global MAZE
    height, width = len(s), len(s[0])
    for row_pos, row in enumerate(s):
        for col_pos, val in enumerate(row):
            adj_row_pos = height - 1-  row_pos
            if val == 'S':
                start = col_pos + adj_row_pos*1j
            elif val == 'E':
                end = col_pos + adj_row_pos*1j
            MAZE[col_pos + adj_row_pos*1j] = val

    MAZE = prune_maze(height,width)

    """
    for y in range(height):
        print(''.join(MAZE[x + 1j*y] for x in range(width)))
    """

    lowest_score = find_score(start, end, direction)
    print(lowest_score)





main()
