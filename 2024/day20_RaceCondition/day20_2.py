#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from itertools import combinations
from queue import Queue

maze = {}

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def run_through_maze(start, end, direction):
    """Find the order of squares in the maze"""
    #Direction hard-coded based on input
    global maze

    maze_path = []
    location = start
    while location != end:
        for rot in [1j, 1, -1j]:
            if maze[location + direction*rot] == '.':
                maze_path.append(location)
                direction *= rot
                location += direction
                break
    #Add in the end
    maze_path.append(location)
    return maze_path

def count_time_saved(maze_path, start, end):
    '''Count how much time is saved with this cheat'''
    global maze
    #Cheat is possible if manhattan distance between start and edcoordinates is <= 20)

    #Time saved is distance avoided along main path, minus number of stes needed (manhattan distance)
    manhattan = abs(start.real - end.real) + abs(start.imag - end.imag)
    if manhattan <= 20:
        return abs(maze_path.index(start) - maze_path.index(end)) - manhattan
    return 0

def main():
    s = get_input('input.txt')
    global maze
    width, height = len(s[0]), len(s)
    for row_pos, row in enumerate(s):
        for col_pos, val in enumerate(row):
            coords = col_pos + row_pos*1j
            if val == 'S':
                start = coords
                val = '.'
            elif val == 'E':
                end = coords
                val = '.'
            maze[coords] = val

    #Order of steps needed to get through path
    maze_path = run_through_maze(start, end, 1j)

    super_savers = 0
    #Try a cheat between every 2 places on the path
    path_pairs = list(combinations(maze_path, 2))
    for path_pair in path_pairs:
        start, end = path_pair[0], path_pair[1]
        time_saved = count_time_saved(maze_path, start, end)
        if time_saved >= 100:
            super_savers += 1
    print(super_savers)


main()
