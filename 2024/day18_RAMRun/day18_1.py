#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from queue import Queue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    space = {}

    max_dim = 70
    for x in range(max_dim + 1):
        for y in range(max_dim + 1):
            space[x + y*1j] = float('inf')
    for byte in s[:1024]:
        byte = byte.split(',')
        space[int(byte[0]) + int(byte[1])*1j] = -1
    space[0] = 0

    #Use djikstra's
    #Could use A* to speed up a bit, but 71x71 should be fairly quick
    paths = Queue()
    paths.put((0, 0))
    while True:
        next_square = paths.get()
        coords, length = next_square[0], next_square[1]
        if coords == max_dim + max_dim*1j:
            print(length)
            sys.exit(0)
        for direction in [1, 1j, -1, -1j]:
            try:
                adj_square = coords + direction
                if space[adj_square] > length + 1:
                    space[adj_square] = length + 1
                    paths.put((adj_square, length + 1))
            except:
                #Out of bounds
                pass
    


main()
