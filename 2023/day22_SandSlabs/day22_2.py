#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd
import queue

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_collapse_bricks(supporting, supported_by, number_of_bricks):
    '''Determine how many bricks in total will collapse'''
    collapsing_bricks = 0

    for i in range(number_of_bricks):
        collapsing_bricks += collapse(i, supporting, supported_by)

    return collapsing_bricks

def collapse(missing_brick, supporting, supported_by):
    '''Count the bricks falling when missing_brick is removed'''

    #Set of bricks currently set to fall
    falling_bricks = {missing_brick}
    bricks_to_kill = queue.Queue()
    bricks_to_kill.put(missing_brick)

    while not bricks_to_kill.empty():
        next_potentially_dead_brick = bricks_to_kill.get()
        is_going_to_fall = True
        #The brick will fall if all supporting bricks are all falling
        for supporting_brick in supported_by[next_potentially_dead_brick]:
            if supporting_brick not in falling_bricks:
                is_going_to_fall = False
                break
            
        if is_going_to_fall or next_potentially_dead_brick == missing_brick:
            #If this brick is gone, the next bricks will be gone too
            for next_brick_up in supporting[next_potentially_dead_brick]:
                bricks_to_kill.put(next_brick_up)
            if is_going_to_fall:
                falling_bricks.add(next_potentially_dead_brick)
        

    #Ignore the removed brick, so -1
    return len(falling_bricks) - 1
    

def main():
    s = get_input('input.txt')
    block_coords = [tuple(map(int,block.replace('~',',').split(','))) for block in s]

    #Sort the blocks by lowest coordinate, this will be the order they fall in
    block_coords.sort(key=lambda block: min(block[2], block[5]))


    #Track the top facing block
    top_blocks = {}

    #Tracks what every block is supporting
    supporting = dd(set)

    #Tracks what every block is supported by
    supported_by = dd(set)

    for block_pos, block in enumerate(block_coords):
        start_x, start_y, start_z, end_x, end_y, end_z = block

        #Check for vertical block
        if start_z != end_z:
            height = abs(end_z - start_z)
            if (start_x, start_y) not in top_blocks:
                #New entry on 0:
                top_blocks[(start_x, start_y)] = (height + 1, block_pos)
            else:
                #Update the mappings, and the new block on top
                last_height, last_block = top_blocks[(start_x, start_y)]
                supporting[last_block].add(block_pos)
                supported_by[block_pos].add(last_block)
                top_blocks[(start_x, start_y)] = (last_height + height + 1, block_pos)

        #Otherwise, it's horizontal
        else:
            highest_to_rest_on = 0
            highest_block = set()
            #Check the lateral positions of all squares
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    try:
                        last_height, last_block = top_blocks[(x, y)]
                        #If new highest block, this is the support
                        if last_height > highest_to_rest_on:
                            highest_to_rest_on = last_height
                            highest_block = set({last_block})
                        #If equal height, it also can support
                        elif last_height == highest_to_rest_on:
                            highest_block.add(last_block)
                    except:
                        continue

            #Update the mappings, and the new block on top
            if highest_to_rest_on != 0:
                for supporting_block in highest_block:
                    supporting[supporting_block].add(block_pos)
                    supported_by[block_pos].add(supporting_block)
                    #print('\t' + str(supporting[supporting_block]))
            #print('\t\t' + str(supported_by[block_pos]))
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    top_blocks[(x, y)] = (highest_to_rest_on + 1, block_pos)





    collapse_count = count_collapse_bricks(supporting, supported_by, len(block_coords))
    print(collapse_count)
main()
