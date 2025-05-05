#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    turns = s[0]
    directions = {}
    for node in s[2:]:
        start, ends = node.split(' = (')
        end1,end2 = ends.split(', ')
        end2 = end2[:-1]
        directions[start] = tuple([end1, end2])

    current_point = 'AAA'

    map_point = 0
    length_of_map = len(turns)

    while current_point != 'ZZZ':
        next_direction = turns[map_point%length_of_map]
        if next_direction == 'L':
            current_point = directions[current_point][0]
        else:
            current_point = directions[current_point][1]
        map_point += 1

    print(map_point)


main()
