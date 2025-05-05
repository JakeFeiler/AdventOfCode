#!/opt/anaconda3/bin/python
#Jake Feiler

import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def climb_up(hill_terrain, current_location, current_height, reachable_peaks):
    '''Find paths upwards from here'''

    #Reached the top
    if current_height == 9:
        reachable_peaks.add(current_location)

    #Check if any of the neighbording paths work
    for direction in (1, -1, 1j, -1j):
        try:
            if hill_terrain[current_location + direction] == current_height + 1:
                reachable_peaks += climb_up(hill_terrain, current_location + direction, current_height + 1, reachable_peaks)
        except:
            pass
    return reachable_peaks

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
    total_score = 0
    for trailhead in trailheads:
        reachable_peaks = set()
        reachable_peaks = climb_up(hill_terrain, trailhead, 0, reachable_peaks)
        total_score += len(reachable_peaks)
    print(total_score)

main()
