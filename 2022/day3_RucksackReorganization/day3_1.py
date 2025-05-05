#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def add_to_total_priority(item):
    'Determine its value'
    ascii_value = ord(item)
    if ascii_value <= 96:
        return ascii_value - 38
    else:
        return ascii_value - 96

def main():
    s = get_input('input.txt')
    total_priority = 0
    for rucksack in s:
        compartment_1, compartment_2 = rucksack[:int(len(rucksack)/2)], rucksack[-1*int(len(rucksack)/2):]
        sorted_c_1, sorted_c_2 = ''.join(sorted(compartment_1)), ''.join(sorted(compartment_2))
        position_in_c2 = 0

        match_found = False
        for item in sorted_c_1:
            if match_found:
                break
            while item >= sorted_c_2[position_in_c2]:
                if item == sorted_c_2[position_in_c2]:
                    total_priority += add_to_total_priority(item)
                    match_found = True
                    break
                else:
                    position_in_c2 += 1

    print(total_priority)


main()
