#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def map_the_type(source_category, destination_categories):
    '''Turn the source # into its mapped number'''
    for destination_category in destination_categories:
        destination_category = list(map(int, destination_category.strip().split(' ')))
        dest_range_start, source_range_start, range_len = destination_category
        if source_range_start <= source_category < source_range_start + range_len:
            destination_category = dest_range_start + (source_category - source_range_start)
            return destination_category

    #Return source categry if not in the mappings
    return source_category



def main():
    s = get_input('input.txt')
    closest_location = None

    #Set the start categories to the seeds
    current_categories = s[0].split(': ')[1].split(' ')

    next_category = []
    for line in s[2:]:
        if line == '':
            #At a blank line, map everything
            current_categories = [map_the_type(int(curr_type), next_category) for curr_type in current_categories]
            next_category = []
        elif line[0].isdigit():
            next_category.append(line)

    #One more time for missing blank line at end
    current_categories = [map_the_type(int(curr_type), next_category) for curr_type in current_categories]
    closest_location = min(current_categories)




    print(closest_location)





main()
