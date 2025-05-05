#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    stream = s[0]
    current_loc = 3
    while current_loc < len(stream):
        last_four = [stream[current_loc], stream[current_loc - 1], stream[current_loc - 2], stream[current_loc - 3]]
        if last_four[0] == last_four[1]:
            current_loc += 3
        elif last_four[2] in (last_four[0], last_four[1]):
            current_loc += 2
        elif last_four[3] in (last_four[0], last_four[1], last_four[2]):
            current_loc += 1
        else:
            print(current_loc + 1)
            return

main()
