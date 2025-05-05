#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]


def map_the_type(source_categories, destination_categories):
    '''Turn the source categories into their mapped numbers'''
    #Now using ranges instead of individual numbers
    output_category_ranges = []


    while len(source_categories) > 0:
        source_range = source_categories.pop()
        source_range_start, source_range_end = source_range[0], source_range[-1]

        #Append raw range to output unless a mapping is found
        found_match = False
        
        for destination_category in destination_categories:
            destination_category = list(map(int, destination_category.strip().split(' ')))
            dest_range_map_start, source_range_map_start, range_len = destination_category
            source_range_map_end = source_range_map_start + range_len

        #Need to keep repeating if categories take up multiple conditions

            #6 possibilites of overlap between the input ranges and the mapping ranges

            #1 Subset
            if source_range_start >= source_range_map_start and source_range_end < source_range_map_end:
                found_match = True
                offset1, offset2 = source_range_start - source_range_map_start, source_range_end - source_range_map_start
                output_category_ranges.append(range(dest_range_map_start + offset1, dest_range_map_start + offset2 + 1))
                break

            #2 Map is subset of input
            elif source_range_start < source_range_map_start and source_range_end > source_range_map_end:
                found_match = True
                output_category_ranges.append(range(dest_range_map_start, dest_range_map_start + range_len + 1))
                source_categories.append(range(source_range_start, source_range_map_start))
                source_categories.append(range(source_range_map_end + 1, source_range_end + 1))
                break

            #3: Input ends midway through mapping
            #Source  123456
            #Mapping    456789
            elif source_range_map_start <= source_range_end < source_range_map_end:
                found_match = True
                if source_range_start != source_range_map_start:
                    source_categories.append(range(source_range_start, source_range_map_start))
                output_category_ranges.append(range(dest_range_map_start, dest_range_map_start + (source_range_end - source_range_map_start) + 1))
                break

            #4: Input stat midway through mapping
            #Mapping  123456
            #Source      456789
            elif source_range_map_start <= source_range_start < source_range_map_end:
                found_match = True
                if source_range_end != source_range_map_end:
                    source_categories.append(range(source_range_map_end, source_range_end + 1))
                output_category_ranges.append(range(dest_range_map_start + (source_range_start - source_range_map_start), dest_range_map_start + range_len))
                break

            #5/6 Disjoint
            elif source_range_start > source_range_map_end or source_range_end < source_range_map_start:
                continue

        #No overlap, add it to the output
        if not found_match:
            output_category_ranges.append(source_range)

    return output_category_ranges


def main():
    s = get_input('input.txt')
    closest_location = None

    #Set the start categories to the seeds
    seed_line = s[0].split(': ')[1].split(' ')
    current_categories = []
    for info_pos in range(len(seed_line)//2):
        seed_start, seed_range = int(seed_line[2*info_pos]), int(seed_line[2*info_pos + 1])
        seeds = range(seed_start, seed_start + seed_range)
        current_categories.append(seeds)

    next_category = []
    for line in s[2:]:
        if line == '':
            #At a blank line, map everything
            current_categories = map_the_type(current_categories, next_category)
            next_category = []
        elif line[0].isdigit():
            next_category.append(line)

    #One more time for missing blank line at end
    current_categories = map_the_type(current_categories, next_category)
    closest_location = min(final_range[0] for final_range in current_categories)

    print(closest_location)
    




main()
