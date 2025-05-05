#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    starting_numbers = input_file.readline().strip().split(',')
    return list(map(int, starting_numbers))

def main():
    starting_numbers = get_input('input.txt')
    positions_said = defaultdict(list)
    for position, number in enumerate(starting_numbers):
        positions_said[number].append(position)
    previous_number = starting_numbers[-1]
    for position in range(len(starting_numbers), 30000000):
        if len(positions_said[previous_number]) < 2:
            previous_number = 0
        else:
            previous_number = positions_said[previous_number][-1] - positions_said[previous_number][-2]
        positions_said[previous_number].append(position)
    print(previous_number)


main()
