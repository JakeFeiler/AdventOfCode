#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_trees(row, column, tree_val, tree_grid):
    '''Count all visible trees in the 4 directions'''
    perm_row = row
    perm_col = column

    max_width = len(tree_grid)
    max_height = len(tree_grid[0])

    trees_seen = 1
    trees_w = 0
    trees_e = 0
    trees_n = 0
    trees_s = 0

    #count trees in all direction.
    #add 1 for each new tree reached, stop counting at bigger tree

    while column > 0:
        trees_w += 1
        column -= 1
        if int(tree_grid[perm_row][column]) >= tree_val:
            column = 0

    column = perm_col
    while column < max_width - 1:
        trees_e += 1
        column += 1
        if int(tree_grid[perm_row][column]) >= tree_val:
            column = max_width

    while row > 0:
        trees_n += 1
        row -= 1
        if int(tree_grid[row][perm_col]) >= tree_val:
            row = 0

    row = perm_row
    while row < max_height - 1:
        trees_s += 1
        row += 1
        #if hit a bigger tree, end the loop
        if int(tree_grid[row][perm_col]) >= tree_val:
            row = max_height

    return trees_seen * trees_w * trees_e * trees_n * trees_s

def main():
    s = get_input('input.txt')
    number_of_columns = len(s[0])
    number_of_rows = len(s)
    seeable_trees = [[1 for c in range (number_of_columns)] for r in range (number_of_rows)]


    tree_heights = []
    for row in s:
        tree_heights.append(row)


    most_trees_seen = 0
    for row_order, row in enumerate(tree_heights):
        for column_order, tree in enumerate(row):
            seeable_trees = count_trees(row_order, column_order, int(tree), tree_heights)
            if seeable_trees > most_trees_seen:
                most_trees_seen = seeable_trees

    print(most_trees_seen)

main()
