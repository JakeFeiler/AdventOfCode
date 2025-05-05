#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def climb_up(hill_terrain, current_location, current_height):
    '''Find paths upwards from here'''

    paths_from_here_to_top = 0
    #Reached the top
    if current_height == 9:
        return True

    #Check if any of the neighbording paths work
    for direction in (1, -1, 1j, -1j):
        try:
            if hill_terrain[current_location + direction] == current_height + 1:
                paths_from_here_to_top += climb_up(hill_terrain, current_location + direction, current_height + 1)
        except:
            pass
    return paths_from_here_to_top

def main():
    s = get_input('input.txt')
    hill_terrain = {}
    trailheads = []
    for row_pos, row in enumerate(s):
        for col_pos, value in enumerate(row):
            coords = col_pos + 1j * (len(s) -1 - row_pos)
            hill_terrain[coords] = int(value)
            if value == '0':
                trailheads.append(coords)
    reachable_peaks = 0
    for trailhead in trailheads:
        reachable_peaks += climb_up(hill_terrain, trailhead, 0)
    print(reachable_peaks)

main()
