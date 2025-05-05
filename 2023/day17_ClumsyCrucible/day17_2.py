#!/opt/anaconda3/bin/python
#Jake Feiler


import sys
import numpy
import time


def find_min_loss(min_paths, blocks):
    '''Get the min path from top left to bottom right'''

    #Height chart
    #0: Fresh start, only first point
    #1-10: Going right
    #11-20: Going down
    #21-31: Going left
    #31-40: Going up

    min_paths[0][0][0] = int(blocks[0][0])
    to_search = []
    first_x_move = 0
    first_y_move = 0
    for i in range(1,5):
        first_x_move += int(blocks[0][i])
        first_y_move += int(blocks[i][0]) 
    to_search.append((0,4,4,first_x_move))
    to_search.append((4,0,14,first_y_move))

    final_row, final_col = len(blocks), len(blocks[0])
    prev_point = (0,0)
    min_path = 0

    while prev_point[0] != final_row - 1 or prev_point[1] != final_col - 1:
        next_point = min(to_search, key = lambda x: x[3])
        to_search.remove(next_point)

        x,y = next_point[0], next_point[1]
        height = next_point[2]
        min_path = next_point[3]

       # if loops_through % 10_000 == 0:
       #     print(loops_through)
       #     print(x,y,height,min_path)
        #min_paths[x][y][height] = min_path


        #Add more points to search to map
        #Look right
        if height not in [10,*range(21,31)]:
            if height in list(range(4,10)):
                new_height = height + 1
                diff = 1
            else:
                new_height = 4
                diff = 4
            #Check to see if this point has been looked at in this direction before
            #If so, skip it. If not, add it to the Djikstra search
            if y < final_col - diff and min_paths[x][y+diff][new_height] == 0:
                shortest_to_next = min_path
                for i in range(1,diff + 1):
                    shortest_to_next += int(blocks[x][y+i])
                min_paths[x][y+diff][new_height] = shortest_to_next
                to_search.append((x, y+diff, new_height, shortest_to_next))

        #Look down
        if height not in (20, *range(31,41)):
            if height in list(range(14,20)):
                new_height = height + 1
                diff = 1
            else:
                new_height = 14
                diff = 4
            if x < final_row -  diff and min_paths[x+diff][y][new_height] == 0:
                shortest_to_next = min_path
                for i in range(1,diff + 1):
                    shortest_to_next += int(blocks[x+i][y])
                min_paths[x+diff][y][new_height] = shortest_to_next
                to_search.append((x+diff, y, new_height, shortest_to_next))

        #Look left
        if height not in (30,*range(1,11)):
            if height in list(range(24,30)):
                new_height = height + 1
                diff = 1
            else:
                new_height = 24
                diff = 4
            if  y >= diff and min_paths[x][y-diff][new_height] == 0:
                shortest_to_next = min_path
                for i in range(1,diff + 1):
                    shortest_to_next += int(blocks[x][y-i])
                min_paths[x][y-diff][new_height] = shortest_to_next
                to_search.append((x, y - diff, new_height, shortest_to_next))

        #Look up
        if height not in (40, *range(11,21)):
            if height in list(range(34,40)):
                new_height = height + 1
            else:
                new_height = 34
                diff = 4
            if x >= diff and min_paths[x-diff][y][new_height] == 0:
                shortest_to_next = min_path
                for i in range(1,diff+1):
                    shortest_to_next += int(blocks[x-i][y])
                min_paths[x-diff][y][new_height] = shortest_to_next
                to_search.append((x-diff, y, new_height, shortest_to_next))

        prev_point = (x, y)

    return min_path


def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    #Plan - use 3D array for Djikstra, with 3rd to coordinate directions
    length = len(s[0])
    width = len(s)
    height = 1 + 4*10

    min_paths = numpy.zeros((width,length,height))

    min_loss = find_min_loss(min_paths, s)

    print(min_loss)


main()
