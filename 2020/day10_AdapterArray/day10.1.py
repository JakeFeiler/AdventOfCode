#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]

def main():
    jolts = get_input('input.txt')
    top_joltage = max(jolts)
    number_of_jolts = len(jolts)
    #x*1 + 3*y = max
    #x + y = number
    #x = number - y
    #number - y + 3*y = max
    #y = (max - number)/2
    #x = number - (max-number)/2
    #x = number*3/2 - max/2
    #Don't forget to add 1 to y for my device

    ones_count = number_of_jolts * 3/2 - top_joltage / 2
    threes_count = (top_joltage - number_of_jolts) / 2
    print(int(ones_count * (threes_count + 1)))

main()
