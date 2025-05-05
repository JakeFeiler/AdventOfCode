#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import itertools

def get_input(text):
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]
        
def main():
    entries = get_input('input.txt')
    for first, second, third in itertools.combinations(entries, 3):
        if first + second + third == 2020:
            print(first*second*third)
            sys.exit(0)

main()
