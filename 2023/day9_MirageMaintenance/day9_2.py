#!/opt/anaconda3/bin/python
#Jake Feiler

#!= 1916822748

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_next_difference(sequence):
    '''Get the next difference in the sequence, per spec'''
    if max(sequence) == 0 and min(sequence) == 0:
        return 0
    next_sequence = list(map(lambda x, y: x - y, sequence[1:], sequence[:-1]))
    return next_sequence[0] - find_next_difference(next_sequence)
    

def main():
    s = get_input('input.txt')

    missing_total = 0
    for line in s:
        sequence = list(map(int, line.split(' ')))
        missing_total += (sequence[0] - find_next_difference(sequence))
    print(missing_total)


main()
