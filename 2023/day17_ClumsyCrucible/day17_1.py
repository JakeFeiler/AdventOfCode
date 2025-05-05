#!/opt/anaconda3/bin/python
#Jake Feiler



import sys
import numpy
import time


def find_min_loss(min_paths, blocks):
    '''Get the min path from top left to bottom right'''

    #Height chart
    #0: Fresh start, only first point
    #1/2/3: Going right
    #4/5/6: Going down
    #7/8/9: Going left
    #10/11/12: Going up

    min_paths[0][0][0] = int(blocks[0][0])
    to_search = []
    to_search.append((0,1,1,int(blocks[0][1])))
    to_search.append((1,0,3,int(blocks[1][0])))

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
        if y != final_col - 1 and height not in (3,7,8,9):
            if height < 3:
                new_height = height + 1
            else:
                new_height = 1
            #Check to see if this point has been looked at in this direction before
            #If so, skip it. If not, add it to the Djikstra search
            if min_paths[x][y+1][new_height] == 0:
                shortest_to_next = min_path + int(blocks[x][y+1])
                min_paths[x][y+1][new_height] = shortest_to_next
                to_search.append((x, y+1, new_height, shortest_to_next))

        #Look down
        if x != final_col - 1 and height not in (6,10,11,12):
            if 4 <= height <= 5:
                new_height = height + 1
            else:
                new_height = 4
            if min_paths[x+1][y][new_height] == 0:
                shortest_to_next = min_path + int(blocks[x+1][y])
                min_paths[x+1][y][new_height] = shortest_to_next
                to_search.append((x+1, y, new_height, shortest_to_next))

        #Look left
        if y != 0 and height not in (9,1,2,3):
            if 7 <= height <= 8:
                new_height = height + 1
            else:
                new_height = 7
            if  min_paths[x][y-1][new_height] == 0:
                shortest_to_next = min_path + int(blocks[x][y-1])
                min_paths[x][y-1][new_height] = shortest_to_next
                to_search.append((x, y - 1, new_height, shortest_to_next))

        #Look up
        if x != 0 and height not in (12,4,5,6):
            if 10 <= height <= 11:
                new_height = height + 1
            else:
                new_height = 10
            if min_paths[x-1][y][new_height] == 0:
                shortest_to_next = min_path + int(blocks[x-1][y])
                min_paths[x-1][y][new_height] = shortest_to_next
                to_search.append((x-1, y, new_height, shortest_to_next))

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
    height = 1 + 4*3

    min_paths = [[[0 for h in range(height)] for w in range(width)] for l in range(length)]
    min_paths = numpy.zeros((length,width,height))

    min_loss = find_min_loss(min_paths, s)

    print(min_loss)


main()
