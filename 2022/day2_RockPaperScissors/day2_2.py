#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import deque

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    total_score = 0
    result_to_point = {'X': 0, 'Y': 3, 'Z': 6}
    points_on_draw = {'A': 1, 'B': 2, 'C': 3}

    for shapes in s:
        opponent, me = shapes.split(' ')
        total_score += result_to_point[me]
        if me == 'X':
            total_score += ((points_on_draw[opponent] + 1) % 3 + 1)
        elif me == 'Y':
            total_score += points_on_draw[opponent]
        else:
            total_score += (points_on_draw[opponent] % 3) + 1

    print(total_score)




main()
