#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import itertools

def get_input(text):
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]
        
def main():
    entries = get_input('input.txt')
    for first, second in itertools.combinations(entries, 2):
        if first + second == 2020:
            print(first*second)
            sys.exit(0)

main()
