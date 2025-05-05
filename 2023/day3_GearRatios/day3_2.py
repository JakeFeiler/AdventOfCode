#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    number_locations = {}
    total_gear_ratio = 0

    for row, row_text in enumerate(s):
        #Loop through, track numbers and coordinates
        number_locations[row] = []
        start_col = -1
        cur_value = 0
        for col, value in enumerate(row_text):
            if value.isdigit():
                cur_value = 10*cur_value + int(value)
                if start_col < 0:
                    start_col = col
            #Populate table if the number has ended
            if cur_value >0 and (not value.isdigit() or col == len(row_text) - 1):
                end_col = col - 1
                #Value, (coordinates)
                number_locations[row].append((cur_value, start_col, end_col, False))
                start_col = -1
                cur_value = 0

    #Loop back through, find adjancies to symbols
    for row, row_text in enumerate(s):
        for col, value in enumerate(row_text):
            if value == '*':
                #No symbols in border, no index issues
                gear_ratio = 1
                gear_count = 0
                for adj_row in range(row - 1, row + 2):
                    #look through all numbers on that row:
                    for number_pos, number_data, in enumerate(number_locations[adj_row]):
                        val, start_col, end_col, already_found = number_data
                        if start_col <= (col + 1) and end_col >= (col - 1):
                            gear_ratio *= val
                            gear_count += 1
                if gear_count == 2:
                    total_gear_ratio += gear_ratio


    print(total_gear_ratio)





main()
