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
        #Trivial to count horizontal counts
        xmas_count += ''.join(row).count('XMAS')
        xmas_count += ''.join(row).count('SAMX')
        
        for col_pos, letter in enumerate(row):
            if letter == 'X':
                far_from_left = col_pos >= 3
                far_from_right = col_pos <= row_length - 4
                far_from_top = row_pos >= 3
                far_from_bottom = row_pos <= col_length - 4             
                #Count Down, and downward diagonals
                if far_from_bottom:
                    xmas_count += grid[row_pos + 1][col_pos] == 'M' and  grid[row_pos + 2][col_pos] == 'A' and grid[row_pos + 3][col_pos] == 'S'
                    if far_from_left:
                        xmas_count += grid[row_pos + 1][col_pos - 1] == 'M' and  grid[row_pos + 2][col_pos - 2] == 'A' and grid[row_pos + 3][col_pos - 3] == 'S'
                    if far_from_right:
                        xmas_count += grid[row_pos + 1][col_pos + 1] == 'M' and  grid[row_pos + 2][col_pos + 2] == 'A' and grid[row_pos + 3][col_pos + 3] == 'S'
                #Count Up, and upward diagonals
                if far_from_top:
                    xmas_count += grid[row_pos - 1][col_pos] == 'M' and  grid[row_pos - 2][col_pos] == 'A' and grid[row_pos - 3][col_pos] == 'S'
                    if far_from_left:
                        xmas_count += grid[row_pos - 1][col_pos - 1] == 'M' and  grid[row_pos - 2][col_pos - 2] == 'A' and grid[row_pos - 3][col_pos - 3] == 'S'
                    if far_from_right:
                        xmas_count += grid[row_pos - 1][col_pos + 1] == 'M' and  grid[row_pos - 2][col_pos + 2] == 'A' and grid[row_pos - 3][col_pos + 3] == 'S'
        
    print(xmas_count)

main()
