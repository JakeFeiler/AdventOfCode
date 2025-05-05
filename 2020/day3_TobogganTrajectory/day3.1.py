#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]
        
def main():
    paths = get_input('input.txt')
    length_of_row = len(paths[0])
    current_column = 0
    trees_hit = 0
    for path in paths:
        if path[current_column % length_of_row] == '#':
            trees_hit += 1
        current_column += 3
    
    print(trees_hit)

main()
