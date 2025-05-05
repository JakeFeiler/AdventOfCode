#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    stream = s[0]
    current_loc = 13
    while current_loc < len(stream):
        last_fourteen = []
        for i in range(14):
            last_fourteen.append(stream[current_loc - i])

        hasnt_found_a_match = True
        for position, signal in enumerate(last_fourteen[1:]):
            if signal in last_fourteen[:position+1]:
                #Can skip ahead appropriate amount depending on where the match was found
                current_loc += (13 - position)
                hasnt_found_a_match = False
                break

        if hasnt_found_a_match:
            print(current_loc + 1)
            return


main()
