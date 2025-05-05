#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    h_distance = 0
    v_distance = 0
    for movement in s:
        direction, distance = movement.split(' ')
        distance = int(distance)
        if direction == 'forward':
            h_distance += distance
        elif direction == 'up':
            v_distance -= distance
        elif direction == 'down':
            v_distance += distance
    print(v_distance * h_distance)


main()
