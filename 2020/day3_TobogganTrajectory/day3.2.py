#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def check_technique(row_movement, col_movement, paths):
    '''Check how many trees are hit moving right with col_movement, down with row_movement'''
    
    length_of_row = len(paths[0])
    current_row = 0
    current_column = 0
    trees_hit = 0
    while current_row < len(paths):
        if paths[current_row][current_column % length_of_row] == '#':
            trees_hit += 1
        current_row += row_movement
        current_column += col_movement
    return trees_hit
        
def main():
    paths = get_input('input.txt')
    total_trees_hit = check_technique(1, 1, paths)
    total_trees_hit *= check_technique(1, 3, paths)
    total_trees_hit *= check_technique(1, 5, paths)
    total_trees_hit *= check_technique(1, 7, paths)
    total_trees_hit *= check_technique(2, 1, paths)

    
    print(total_trees_hit)

main()
