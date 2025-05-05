#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import itertools

#>2935

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def count_ways(spring_status, bad_spring_counts):
    '''Count how many possible configurations there are'''
    total_configurations = 0
    total_springs = len(spring_status)
    total_defects = sum(bad_spring_counts)

    #Use Stars and Bars technique to generate all possible strings, compare each one to existinig string

    length_of_stars = total_springs - total_defects
    for combination in itertools.combinations(list(range(length_of_stars + 1)), len(bad_spring_counts)):
        stars_and_bars_string = ['*'] * (length_of_stars)
        for indice in combination[::-1]:
            stars_and_bars_string.insert(indice, '|')
        total_configurations += validate_config(stars_and_bars_string, spring_status, bad_spring_counts)
    return total_configurations

def validate_config(stars_and_bars_string, spring_status, bad_spring_counts):
    '''Given a config like '**|*|*', see if it works with the input'''
    current_bad_batch = 0
    current_spring_point = 0
    for icon in stars_and_bars_string:
        
        #Reject if test has good, when status has a bad
        if icon == '*':
            if spring_status[current_spring_point] == '#':
                return 0
            current_spring_point += 1            
        #If a bad indication, check the next group of springs for any goods
        #icon == '|'
        else:
            for _ in range(bad_spring_counts[current_bad_batch]):
                if spring_status[current_spring_point] == '.':
                    return 0
                current_spring_point += 1
            current_bad_batch += 1

    #It works! Add 1
    return 1

def main():
    s = get_input('input.txt')
    possible_ways = 0
    for row_of_spring in s:
        spring_status, spring_counts = row_of_spring.split(' ')
        spring_counts = list(map(int,spring_counts.split(',')))
        possible_ways += count_ways(spring_status, spring_counts)
    print(possible_ways)


main()
