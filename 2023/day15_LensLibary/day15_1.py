#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def hash_algo(step):
    '''Run the algorithm as instructed'''
    value = 0
    for character in step:
        value += ord(character)
        value *= 17
        value %= 256
    #print(step, value)
    return value

def main():
    s = get_input('input.txt')
    sequence = "".join(s).split(',')

    total_sum = 0
    for step in sequence:
        total_sum += hash_algo(step)
    print(total_sum)


main()
