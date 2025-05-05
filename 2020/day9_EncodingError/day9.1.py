#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from itertools import combinations

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]

def check_data(data, line_num, current_list):
    '''determine if next number is a sum of two of the previous 25 numbers'''
    value_to_check = data[line_num]
    value_pairs = combinations(data, 2)
    for pair in value_pairs:
        if value_to_check == sum(pair):
            current_list = current_list[1:]
            current_list.append(value_to_check)
            return check_data(data, line_num + 1, current_list)
    return value_to_check

def main():
    xmas_data = get_input('input.txt')
    preamble = xmas_data[:25]
    invalid_value = check_data(xmas_data, 25, preamble)
    print(invalid_value)

main()
