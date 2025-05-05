#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from itertools import combinations

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [int(line.strip()) for line in input_file]

def find_weakness(data, line_num, total, faulty_value):
    '''Find the list of numbers that sum to value from part 1'''
    current_sum = sum(total)

    #if underestimating value, add the value to the list
    if current_sum < faulty_value:
        total.append(data[line_num])
        return find_weakness(data, line_num + 1, total, faulty_value)

    # if overestimating, remove the first value
    elif current_sum > faulty_value:
        return find_weakness(data, line_num, total[1:], faulty_value)

    #else, we have a match
    return min(total) + max(total)

def main():
    xmas_data = get_input('input.txt')
    faulty_value = 133015568 #from part 1
    encryption_weakness = find_weakness(xmas_data, 0, [], faulty_value)
    print(encryption_weakness)

main()
