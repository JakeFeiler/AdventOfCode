#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def ways_to_make(desired, avail_patterns_by_length, longest_pattern):
    '''Count the number of ways to make the desired pattern'''

    #Dynamic Programming approach
    #Track how many ways there are to use this many stripes (offset by one)
    #0 index = 1 stripe, 1 index = 2 stripes, etc
    possibilities_to_stripe_count = [0]*len(desired)
    for possibility in range(len(desired)):
        for pattern_length in range(1, longest_pattern + 1):
            if possibility + 1 - pattern_length < 0:
                #Can't use a pattern length this long this early
                #i.e. - possibility = 3, pl = 5
                #Too early to begin with a length of 5
                continue
            """
            if possibility + pattern_length > len(desired):
                #Continue here, not enough room to fit this pattern in
                continue
            """
            end_point = possibility + 1
            start_point = end_point - pattern_length
            #We found the pattern, dynamically add it to the count
            if desired[start_point:end_point] in avail_patterns_by_length[pattern_length - 1]:
                #Add 1 to possibile ways if this is the first pattern making the design
                if pattern_length - 1 == possibility:
                    possibilities_to_stripe_count[possibility] += 1
                #Otherwise, dynamically add to possibilities that got to this point
                else:
                    possibilities_to_stripe_count[possibility] += possibilities_to_stripe_count[possibility - pattern_length]

    return possibilities_to_stripe_count[-1]

def main():
    s = get_input('input.txt')
    avail_patterns = s[0].split(', ')
    desired = s[2:]
    longest_pattern = max([len(p) for p in avail_patterns])

    #Sort patterns by length to speed lookup
    #(Dictionary works too, and a bit quicker)
    avail_patterns_by_length = [[] for i in range(longest_pattern)]
    for pattern in avail_patterns:
        avail_patterns_by_length[len(pattern) - 1].append(pattern)

    possible_ways = 0
    for desired_design in desired:
        possible_ways += ways_to_make(desired_design, avail_patterns_by_length, longest_pattern)
    print(possible_ways)


main()
