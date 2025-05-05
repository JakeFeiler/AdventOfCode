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
    aim = 0
    for movement in s:
        direction, distance = movement.split(' ')
        distance = int(distance)
        if direction == 'forward':
            h_distance += distance
            v_distance += distance * aim
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
    print(v_distance * h_distance)


main()
