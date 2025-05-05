#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from queue import Queue
from copy import deepcopy

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_path(space):
    #Use djikstra's
    #Could use A* to speed up a bit, but 71x71 should be fairly quick
    max_dim = 70
    paths = Queue()
    paths.put((0, 0))
    while not paths.empty():
        next_square = paths.get()
        coords, length = next_square[0], next_square[1]
        if coords == max_dim + max_dim*1j:
            return True
        for direction in [1, 1j, -1, -1j]:
            try:
                adj_square = coords + direction
                if space[adj_square] > length + 1:
                    space[adj_square] = length + 1
                    paths.put((adj_square, length + 1))
            except:
                #Out of bounds
                pass

    #Can't explore more, and couldn't reach the end
    return False

def main():
    s = get_input('input.txt')
    orig_space = {}

    max_dim = 70
    for x in range(max_dim + 1):
        for y in range(max_dim + 1):
            orig_space[x + y*1j] = float('inf')
    for byte in s[:1024]:
        byte = byte.split(',')
        orig_space[int(byte[0]) + int(byte[1])*1j] = -1
    orig_space[0] = 0

    for b in s[1025:]:
        byte = b.split(',')
        orig_space[int(byte[0]) + int(byte[1])*1j] = -1
        space = deepcopy(orig_space)
        if not find_path(space):
            print(b)
            sys.exit(0)
        del space




main()
