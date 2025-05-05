#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
HEIGHT = 0
WIDTH = 0
GARDEN = {}

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_dimensions(location, label, explored_lands, area, perimeter):
    '''Try to find more land to explore'''
    directions = [1, -1, -1j, 1j]

    #Look in all direction, recurse if it's the same label
    for direction in directions:
        try:
            new_pos = location + direction
            adjacent_plot = GARDEN[new_pos]
            if adjacent_plot == label:
                if (new_pos) not in explored_lands:
                    #We can add more if it's the same label and not yet visited
                    explored_lands.add(new_pos)
                    explored_lands, area, perimeter = find_dimensions(new_pos, label, explored_lands, area + 1, perimeter)
            else:
                #Hit a different region, so this is a fence
                perimiter += 1

        except:
            #Didn't work, this is the edge, so a fence
            perimeter += 1
    return explored_lands, area, perimeter

def main():
    s = get_input('input.txt')
    global HEIGHT, WIDTH, GARDEN
    HEIGHT, WIDTH = len(s), len(s[0])

    GARDEN = {}
    #Use explored_land to see what plots still need to be looked at
    explored_land = {}

    price = 0
    for row_pos, row in enumerate(s):
        for col_pos, crop in enumerate(row):
            GARDEN[col_pos + 1j*(HEIGHT - 1 - row_pos)] = crop
            explored_land[col_pos + 1j*(HEIGHT - 1 - row_pos)] = False
    for garden_row in range(WIDTH):
        for garden_col in range(WIDTH):
            plot = garden_row + 1j*garden_col
            if not explored_land[plot]:
                label = GARDEN[plot]
                lands_in_this_region = {plot}
                lands_in_this_region, area, perimeter = find_dimensions(plot, label, lands_in_this_region, 1, 0)
                price += area * perimeter
                #Belatedly realization - len(lands_in_this_region) = area
                for found_land in lands_in_this_region:
                    explored_land[found_land] = True
    print(price)




main()
