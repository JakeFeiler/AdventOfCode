#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math
from collections import defaultdict as dd

stone_converter = dd(list)

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def blink(current_stones_counter, blinks):
    '''Iterate the stones'''
    global stone_converter
 
    blinked_stones = dd(int)
    for i in range(blinks):
        #Use the current_stones_counter to track repeat values
        for stone in current_stones_counter:
            #print(len(current_stones))
            #print(stone, type(stone))
            if stone not in stone_converter:
                if stone == 0:
                    new_val = [1]
                elif math.floor(math.log(stone + 0.1, 10)) % 2 == 1:
                    string_stone = str(stone)
                    new_val = [int(string_stone[:len(string_stone)//2]), int(string_stone[len(string_stone)//2:])]
                else:
                    new_val = [stone * 2024]
                stone_converter[stone] = new_val
            created_values = stone_converter[stone]
            #For all of the new values (1 or 2), increase by how many there were of the previous stone
            for new_value in created_values:
                blinked_stones[new_value] += current_stones_counter[stone]
        current_stones_counter = blinked_stones
        blinked_stones = dd(int)

    return sum(current_stones_counter.values())

def main():
    stones = list(map(int,get_input('input.txt')[0].split(' ')))
    stone_counter = dd(int)

    #Initialize a dict with the counts. Not using counter so I can manipulate values
    for stone in stones:
        stone_counter[stone] += 1

    blink_count = 75
    length_of_stones = blink(stone_counter, blink_count)
        
    print(length_of_stones)

main()
