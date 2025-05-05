#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_distance(first_point, second_point, empty_rows, empty_cols):
    '''Find the manhattan distance, double counting the empty rows/cols'''
    x1, y1 = first_point
    x2, y2 = second_point
    distance = 0
    distance += abs(x2 - x1) +  abs(y1 - y2)
    for empty_row in empty_rows:
        if (x1 <= empty_row <= x2) or (x1 >= empty_row >= x2):
            distance += 999_999
    for empty_col in empty_cols:
        if (y1 <= empty_col <= y2) or (y1 >= empty_col >= y2):
            distance += 999_999
    return distance

def main():
    s = get_input('input.txt')

    empty_rows = [_ for _ in range(len(s))]
    empty_cols = [_ for _ in range(len(s[0]))]

    galaxies = []
    for row_pos, row in enumerate(s):
        for col_pos, square in enumerate(row):
            if square == '#':
                galaxies.append([row_pos, col_pos])
                try:
                    empty_rows.remove(row_pos)
                except:
                    pass
                try:
                    empty_cols.remove(col_pos)
                except:
                    pass

    total_distances = 0
    for first_pos, first_galaxy in enumerate(galaxies):
        for second_galaxy in galaxies[first_pos + 1:]:
            total_distances += find_distance(first_galaxy, second_galaxy, empty_rows, empty_cols)
    print(total_distances)

main()
