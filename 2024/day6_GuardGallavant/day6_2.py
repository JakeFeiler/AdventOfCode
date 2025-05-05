#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from copy import deepcopy

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def does_create_loop(new_lab, position):
    '''Figure out if a loop is made this way'''
    direction = 0 + 1j
    found_spots = set()
    while True:
        #Been here/same way before, a loop!
        if (position, direction) in found_spots:
            return True
        else:
            found_spots.add((position, direction))
        try:
            #Bug found that part 1 missed - allow for backtracking in dead ends
            next_pos = position + direction
            if new_lab[next_pos] == '#':
                direction *= (0 - 1j)
            else:
                position = next_pos
        except:
            #Kill once off the map - we did't loopp
            return False

def main():
    #We can start the same as part 1, as only the spots on the route are candidates
    s = get_input('input.txt')
    position = []
    #Find the start, and set the complex map
    lab = {}
    for row_pos, row in enumerate(s):
        for col_pos, value in enumerate(row):
            lab[col_pos + 1j * (len(s) - 1 - row_pos)] = value
            if value == '^':
                position = col_pos + 1j * (len(s) - 1 - row_pos)
                start_position = position
    #Use the set to track visited squares
    found_spots = set()
    #Start by going north -> right turn is multiplying direction by -i
    direction = 0 + 1j
    while True:
        found_spots.add(position)
        try:
            next_pos = position + direction
            if lab[next_pos] == '#':
                direction *= (0 - 1j)
            position += direction
        except:
            #Kill once off the map
            break

    possible_blocks = 0
    counter = 0
    found_spots.remove(start_position)
    for spot in found_spots:
        counter += 1
        lab_test = deepcopy(lab)
        lab_test[spot] = '#'
        possible_blocks += does_create_loop(lab_test, start_position)
        del lab_test
    print(possible_blocks)

main()
