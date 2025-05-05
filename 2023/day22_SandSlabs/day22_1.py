#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_disintegratable_bricks(supporting, supported_by, number_of_bricks):
    '''Determine how many bricks can be removed'''
    killable_bricks = 0

    #Brick can be disintegrated if - for every brick it's "supporting", there's multiple "supported by"
    for brick in range(number_of_bricks):
        #Ex: Brick A is support
        #Check what it supports (D & E)
        #Check if multiple things support D AND E
        killable = True
        bricks_being_supported = supporting[brick]
        if len(bricks_being_supported) == 0:
            killable_bricks += 1
            continue
        for brick_being_supported in bricks_being_supported:
            support_for_supported_brick = supported_by[brick_being_supported]
            #Not killable if a supported brick has just 1 supported
            if len(support_for_supported_brick) == 1:
                killable = False
        if killable:
            killable_bricks += 1
 
    return killable_bricks

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
                #A block of no z change adds height of 1, even though the diff is 1
                #Therefore, add an extra 1 to the new height
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
            for x in range(start_x, end_x + 1):
                for y in range(start_y, end_y + 1):
                    top_blocks[(x, y)] = (highest_to_rest_on + 1, block_pos)





    disintegrable_count = count_disintegratable_bricks(supporting, supported_by, len(block_coords))
    print(disintegrable_count)
main()
