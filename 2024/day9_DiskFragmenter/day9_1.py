#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file][0]

def populate_the_system(disk_map):
    '''Create a string of IDs, ignoring spaces'''
    full_filesystem = []
    for pos, value in enumerate(disk_map):
        if pos % 2 == 0:
            full_filesystem += [pos//2]*int(value)
    return full_filesystem

def merge_files(system, disk_map):
    '''Create the final string'''
    final = []
    forward_counter = 0
    backward_counter = len(system) - 1
    #Add digits from each until at the same point

    #Index into the map
    disk_map_counter = 0

    remaining_spaces_to_add = 0
    take_from_front = False
    while forward_counter <= backward_counter:
        #We've used up this value in the disk map
        #Take from front - take the IDs in ascending order
        #Take from back - take the IDS in descending order (to fill empty)
        if remaining_spaces_to_add == 0:
            take_from_front = not take_from_front
            remaining_spaces_to_add = int(disk_map[disk_map_counter])
            disk_map_counter += 1
            continue

        if take_from_front:
            final.append(system[forward_counter])
            forward_counter += 1
        else:
            final.append(system[backward_counter])
            backward_counter -= 1
        remaining_spaces_to_add -= 1
    return final
        

def main():
    disk_map = get_input('input.txt')

    full_filesystem = populate_the_system(disk_map)
    combined_system = merge_files(full_filesystem, disk_map)
    checksum = 0
    for pos, value in enumerate(combined_system):
        checksum += pos * value
    print(checksum)

main()
