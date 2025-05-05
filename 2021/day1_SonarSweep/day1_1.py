#!/opt/anaconda3/bin/python
#Jake Feiler

#Weird bug, coming up 1 short. Oh well

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    depths = get_input('input.txt')
    depth_increase_count = 0
    prev_depth = depths[0]
    for depth in depths[1:]:
        if depth > prev_depth:
            depth_increase_count += 1
        prev_depth = depth
    print(depth_increase_count)


main()
