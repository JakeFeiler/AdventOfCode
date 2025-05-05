#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import Counter

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    locs_1 = [int(id[:5]) for id in s]
    locs_2 = [int(id[-5:]) for id in s]

    loc_2_counts = Counter(locs_2)

    sim_score = 0
    for loc in locs_1:
        sim_score += loc * loc_2_counts[loc]
    print(sim_score)

main()
