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
                for row_dir in range(-1, 2):
                    for col_dir in range(-1, 2):
                        if row_dir == 0 and col_dir == 0:
                            continue
                        look_seat_row, look_seat_col = row + row_dir, col + col_dir
                        while 0 <= look_seat_row < row_count and 0 <= look_seat_col < col_count:
                            if previous_seating_chart[look_seat_row][look_seat_col] == '#':
                                filled_count += (previous_seating_chart[look_seat_row][look_seat_col] == '#')
                                break
                            if previous_seating_chart[look_seat_row][look_seat_col] == 'L':
                                break
                            look_seat_row += row_dir
                            look_seat_col += col_dir
                if filled_count == 0 and seat == 'L':
                    change_happened = True
                    seating_chart[row][col] = '#'
                elif filled_count >= 5 and seat == '#':
                    change_happened = True
                    seating_chart[row][col] = 'L'

    occupied_seats = 0
    for row in seating_chart:
        occupied_seats += row.count('#')
    print(occupied_seats)


main()
