#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    locs_1 = [int(id[:5]) for id in s]
    locs_2 = [int(id[-5:]) for id in s]

    locs_1.sort()
    locs_2.sort()

    total_distance = 0
    for pos in range(len(locs_1)):
        #print(locs_1[pos], locs_2[pos])
        total_distance += abs(locs_1[pos]  - locs_2[pos])
    print(total_distance)


main()
