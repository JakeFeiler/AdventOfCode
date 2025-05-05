#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math
#Not very efficent code

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file][0]

def populate_the_system(disk_map):
    '''Create a string of IDs, in accordance with specs'''
    starting_filesystem = []
    for pos, value in enumerate(disk_map):
        if pos % 2 == 0:
            starting_filesystem += [pos//2]*int(value)
        else:
            starting_filesystem += '.'*int(value)
    return starting_filesystem

def merge_files(system, disk_map):
    '''Create the final system'''
    final = []
    backward_counter = len(disk_map) - 1
    start_of_file = len(system)
    #Loop back through backward counter until all files considered
    #Some overkill at some point, looking at already filled space, but not going to optimize stop here

    while backward_counter > 0:
        #Going backward, id is dropping (divide by 2, as every other is a skip
        id_value = backward_counter//2

        size_of_file = int(disk_map[backward_counter])
        start_of_file -= size_of_file

        #Check for a valid insertion spot for the file somewhere before it in the system
        for position in range(start_of_file - size_of_file + 1):
            if all(value == '.' for value in system[position: position + size_of_file]):
                #If a file fits here, insert it and delete it from the system
                system[position:position + size_of_file] = [id_value]*size_of_file
                system[start_of_file:start_of_file + size_of_file] = '.'*size_of_file
                break
        #Ignore space caused by emptiness - more skipping will happen during next loop
        start_of_file -= int(disk_map[backward_counter - 1])
        backward_counter -= 2

    return system


def main():
    disk_map = get_input('input.txt')

    starting_filesystem = populate_the_system(disk_map)
    combined_system = merge_files(starting_filesystem, disk_map)
    checksum = 0
    for pos, value in enumerate(combined_system):
        if value != '.':
            checksum += pos * value
    print(checksum)

main()
