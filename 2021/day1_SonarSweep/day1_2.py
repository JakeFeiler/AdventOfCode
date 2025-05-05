#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

#bug, coming up short by 3. Error with input?

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    depths = get_input('input.txt')
    depth_increase_count = 0

    #Only need to compare with depth from 3 ago
    #'3 ago' is being subtracted, new one is being added
    prev_depth = depths[0]
    for depth_index, depth in enumerate(depths[3:]):
        #print(depth, prev_depth)
        if depth > prev_depth:
            depth_increase_count += 1
        #enumerate starts at, but really counting 3 ahead
        #Then, need to back 2 from there. 3 - 2 = +1
        prev_depth = depths[depth_index + 1]
    print(depth_increase_count)


main()
