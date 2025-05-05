#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def can_be_made(desired, avail_patterns, longest_pattern):
    '''Determine if another pattern can be made'''
    #We've matched the whole thing
    if desired == '':
        return True
    can_match = False
    for length in range(1, min(len(desired), longest_pattern) + 1):
        needed = desired[:length]
        if needed in avail_patterns:
            #A match is found for the first part of the pattern, try continuing
            can_match = can_match or can_be_made(desired[length:], avail_patterns, longest_pattern)
            if can_match:
                return True
    #No matches for the next part
    return False


def main():
    s = get_input('input.txt')
    avail_patterns = s[0].split(', ')
    desired = s[2:]
    longest_pattern = max([len(p) for p in avail_patterns])

    possible_designs = 0
    for desired_design in desired:
        if can_be_made(desired_design, avail_patterns, longest_pattern):
            possible_designs += 1
    print(possible_designs)


main()
