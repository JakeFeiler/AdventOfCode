#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    total = 0

    for card in s:
        card_info = card.split(': ')[1]
        winning_numbers, my_numbers = card_info.split(" | ")
        #Split on the spaces, get rid of nulls
        winning_numbers = [elem for elem in winning_numbers.strip().split(' ') if elem]
        my_numbers = [elem for elem in my_numbers.strip().split(' ') if elem]

        matches = 0
        my_number_dict = dd(int)
        my_number_dict.setdefault('missing_key', 0)
        for my_number in my_numbers:
            my_number_dict[my_number.strip()] += 1

        for winning_number in winning_numbers:
            matches += my_number_dict[winning_number]

        if matches > 0:
            total += 2**(matches - 1)

    print(total)

main()
