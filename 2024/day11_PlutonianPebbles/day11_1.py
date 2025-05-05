#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def blink(current_stones):
    '''Iterate the stones'''
    after_blink = []
    for stone in current_stones:
        #print(stone, type(stone))
        if stone == 0:
            after_blink.append(1)
        elif math.floor(math.log(stone + 0.1, 10)) % 2 == 1:
            #print(math.floor(math.log(stone + 0.1)) % 2)
            string_stone = str(stone)
            after_blink.append(int(string_stone[:len(string_stone)//2]))
            after_blink.append(int(string_stone[len(string_stone)//2:]))
        else:
            after_blink.append(stone * 2024)
    return after_blink

def main():
    stones = list(map(int,get_input('input.txt')[0].split(' ')))
    blink_count = 25
    for _ in range(blink_count):
        stones = blink(stones)
    print(len(stones))

main()
