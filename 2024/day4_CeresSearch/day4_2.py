#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    xmas_count = 0


    grid = get_input('input.txt')
    row_length = len(grid[0])
    col_length = len(grid)
    for row_pos, row in enumerate(grid):
        for col_pos, letter in enumerate(row):
            if letter == 'A' and 0 < col_pos < row_length - 1 and 0  < row_pos < col_length - 1:
                corner_values = [grid[row_pos - 1][col_pos - 1], grid[row_pos - 1][col_pos + 1], grid[row_pos + 1][col_pos - 1], grid[row_pos + 1][col_pos + 1]]
                #Length of list 4 of the corners
                #Need 2 M's, 2 S's, and the oppposites don't match
                xmas_count += corner_values.count('M') == 2 and corner_values.count('S') == 2 and corner_values[0] != corner_values[3]
        
    print(xmas_count)

main()
