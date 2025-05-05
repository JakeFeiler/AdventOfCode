#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import itertools
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_ways(spring_status, bad_spring_counts):
    '''Count how may ways there are, using crude dynamic programming'''

    #Number of ?s we can place on (in order to help enforce placement on #) 
    degrees_of_freedom = sum(bad_spring_counts) - spring_status.count("#")

    #found_ways shouldn't include the ways just placed, in order to prevent blocks of bad springs touching
    found_ways_counter = [[0 for a in range(degrees_of_freedom+1)] for b in range(len(bad_spring_counts)+1)]
    found_ways_counter[0][0] = 1
    just_placed_ways = [[[0 for a in range(len(spring_status))] for b in range(degrees_of_freedom+1)] for c in range(len(bad_spring_counts))]

    for pos, spring in enumerate(spring_status):
        #If spring is good, can add all just placed to final dictionary
        if spring != '.':
            #Try to place a batch of springs starting here
            #Only if previous char wasn't a #
            if pos == 0 or spring_status[pos - 1] != '#':
                try:
                    next_good = spring_status[pos:].index('.')
                except:
                    next_good = len(spring_status) - pos
                for bad_spring_num, bad_spring_length in enumerate(bad_spring_counts):
                    if bad_spring_length <= next_good:
                        #Only place if character after placed spring isn't a #
                        if next_good == bad_spring_length or spring_status[pos + bad_spring_length] != '#':
                            used_options = spring_status[pos: pos + bad_spring_length].count('?')
                            for already_used_options in range(degrees_of_freedom - used_options + 1):
                                just_placed_ways[bad_spring_num][already_used_options + used_options][pos - 1 + bad_spring_length] = found_ways_counter[bad_spring_num][already_used_options]

        for ways_up_to_n in range(len(found_ways_counter) - 1):
            for degree in range(0,degrees_of_freedom+1):
                found_ways_counter[ways_up_to_n + 1][degree] += just_placed_ways[ways_up_to_n][degree][pos-1]


    #Add in the ways involving placing a string in the end
    found_ways_counter[-1][-1] += just_placed_ways[-1][-1][-1]


    return(found_ways_counter[len(bad_spring_counts)][-1])


def main():
    s = get_input('input.txt')
    possible_ways = 0
    for row_of_spring in s:
        spring_status, spring_counts = row_of_spring.split(' ')
        spring_counts = list(map(int,spring_counts.split(',')))
        spring_status = '?'.join([spring_status]*5)
        spring_counts = spring_counts*5
        possible_ways += count_ways(spring_status, spring_counts)
    print(possible_ways)


main()
