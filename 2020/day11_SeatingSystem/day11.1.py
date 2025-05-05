#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [list(line.strip()) for line in input_file]

def main():
    seating_chart = get_input('input.txt')
    row_count = len(seating_chart)
    col_count = len(seating_chart[0])

    change_happened = True
    while change_happened:
        change_happened = False
        previous_seating_chart = list(map(list, seating_chart))
        for row in range(row_count):
            for col in range(col_count):
                seat = previous_seating_chart[row][col]
                if seat == '.':
                    seating_chart[row][col] = '.'
                    continue
                filled_count = 0
                for adj_row in range(-1, 2):
                    for adj_col in range(-1, 2):
                        if (adj_row != 0 or adj_col != 0):
                            row_index = row + adj_row
                            col_index = col + adj_col
                            if row_index < 0 or row_index >= row_count or col_index < 0 or col_index >= col_count:
                                continue
                            #print(row, col, row_index, col_index)
                            filled_count += (previous_seating_chart[row_index][col_index] == '#')
                if filled_count == 0 and seat == 'L':
                    change_happened = True
                    seating_chart[row][col] = '#'
                elif filled_count >= 4 and seat == '#':
                    change_happened = True
                    seating_chart[row][col] = 'L'

    occupied_seats = 0
    for row in seating_chart:
        occupied_seats += row.count('#')
    print(occupied_seats)


main()
