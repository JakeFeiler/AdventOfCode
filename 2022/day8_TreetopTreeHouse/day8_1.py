#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def update_sightings(line, row_num, col_num, tracking_sights):
    '''Given a line of trees, update the tracking sights, both backwards and forwards'''
    min_val_first = -1
    min_val_second = -1

    if row_num == None:
        #tracking a column
        for row, tree in enumerate(line):
            tree = int(tree)
            if tree > min_val_first:
                min_val_first = tree
                tracking_sights[row][col_num] = 1

        #Also populate it backward
        length = len(line) - 1
        for row, tree in enumerate(line[::-1]):
            tree = int(tree)
            if tree > min_val_second:
                min_val_second = tree
                tracking_sights[length - row][col_num] = 1
    else:
        #tracking a row
        for column, tree in enumerate(line):
            tree = int(tree)
            if tree > min_val_first:
                min_val_first = tree
                tracking_sights[row_num][column] = 1

        #Also populate it backward
        length = len(line) - 1
        for column, tree in enumerate(line[::-1]):
            tree = int(tree)
            if tree > min_val_second:
                min_val_second = tree
                tracking_sights[row_num][length - column] = 1


    return tracking_sights

def main():
    s = get_input('input.txt')
    number_of_columns = len(s[0])
    number_of_rows = len(s)
    tracking_sights = [[0 for c in range (number_of_columns)] for r in range (number_of_rows)]


    tree_heights = []
    for row in s:
        tree_heights.append(row)

    for row_order, row in enumerate(tree_heights):
        tracking_sights = update_sightings(list(row), row_order, None, tracking_sights)
        #print(tracking_sights)


    for column_number in range(number_of_columns):
        column = [row[column_number] for row in tree_heights]
        tracking_sights = update_sightings(column, None, column_number, tracking_sights)

    trees_seen = 0
    count = 0
    for row in tracking_sights:
        for is_tree_seen in row:
            trees_seen += is_tree_seen

    print(trees_seen)

main()
