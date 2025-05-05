#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
import math
HEIGHT = 0
WIDTH = 0
GARDEN = {}

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def find_dimensions(location, label, explored_lands, area, edges):
    '''Try to find more land to explore'''
    directions = [1, -1, -1j, 1j]
    #For part 2, use another grid of 2(N+1)X2(N+1) to calculate found edges
    #Then, use edges to calculate number of edges
    #Also record which direction is the exterior
    #Use this map, with plots filling in empty squares, edges at - & |
    #Origin is at bottom left empty square (lowest index is -1)
    '''
    .-.-.-.
    | | | |
    .-.-.-.
    | | | |
    .-.-.-.
    | | | |
    .-.-.-.
    '''
    #2 bigger in both directions -> add 1 to OG coordinates, then add direction

    #Look in all direction, recurse if it's the same label
    for direction in directions:
        try:
            new_pos = location + direction
            adjacent_plot = GARDEN[new_pos]
            if adjacent_plot == label:
                if new_pos not in explored_lands:
                    #We can add more if it's the same label and not yet visited
                    explored_lands.add(new_pos)
                    explored_lands, area, edges = find_dimensions(new_pos, label, explored_lands, area + 1, edges)
            else:
                #Hit a different region, so this is a fence
                edges.add(2*location+direction)


        except:
            #Didn't work, this is the edge, so a fence
            edges.add(2*location+direction)
    return explored_lands, area, edges

def calculate_sides_from_edges(edges):
    '''Given these edges, count the number of sides'''
    #distance = 1: same direction
    #distance = root(2): a change in direction
    #otherwise: too far away
    starting_edge = edges.pop()
    current_edge = starting_edge
    side_count = 0

    #To handle cases of accidentally doubling back near crosssroads, use this to track the relevant edges
    crossroads_edges = []

    while len(edges) > 0:
        candidates = []
        for edge in edges:
            #candidates: all unexplored edges that share a corner

            #Constraint imposed by self-system:
            #Adjacent if distance is 2, and (reals are identical and odd OR complex is identical and odd)
            #That way, fences that are opposite each other won't be counted
            #Turns are opposite sides of square (so root(2) distance)
            if abs(edge - current_edge) == math.sqrt(2):
                candidates.append((edge, 'T'))
            #Prepending straight lines
            elif  abs(edge - current_edge) == 2 and ((edge.real == current_edge.real and edge.real%2 == 1) or (edge.imag == current_edge.imag and edge.imag%2 == 1)):
                candidates.insert(0, ((edge, 'S')))

        #1 candidates - forced to take the only edge that continues
        #2 candidates - choice (such as start), shouldn't matter
        #3 candidates - an intersection. Go straight through, and add 2 to side count
        #spefically, back to back 3's as we cross through, so add 1 each time

        #4 candidates - a crossroads at start. Tricky scenario, let's just try a different edge
        if len(candidates) == 4:

            #Also replace starting edge if we picked it first
            replace_starter = False
            if current_edge == starting_edge:
                replace_starter = True

            edges.add(current_edge)
            current_edge = edges.pop()
            if replace_starter:
                starting_edge = current_edge
            continue
        if len(candidates) == 3:
            side_count += 1




        if len(candidates) >= 1:
            next_edge = candidates[0]
    
            #Special check for 3-border, don't double back to the crossroads
            if len(candidates) == 3:
                for neigh_edge in candidates[::-1]:
                    if neigh_edge not in crossroads_edges:
                        next_edge = neigh_edge
                        
                #Remember the non-used edges, don't visit them again unless needed
                candidates.remove(next_edge)
                crossroads_edges += candidates
            #The perimeter turns, add a side
            if next_edge[1] == 'T':
                side_count += 1
            current_edge = next_edge[0]
            edges.remove(current_edge)

        #Couldn't find another adjacent edge - that means a loop was completed.
        #Check the starting edge connection, and pop a new one.
        if len(candidates) == 0:
            if abs(starting_edge - current_edge) == math.sqrt(2):
                side_count += 1
            starting_edge = edges.pop()
            current_edge = starting_edge


    #Check the starting edge connection
    if abs(starting_edge - current_edge) == math.sqrt(2):
        side_count += 1
    return side_count

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
                edges = set()
                lands_in_this_region, area, edges = find_dimensions(plot, label, lands_in_this_region, 1, edges)
                sides = calculate_sides_from_edges(edges)
                price += area * sides
                for found_land in lands_in_this_region:
                    explored_land[found_land] = True
    print(price)
#>866599





main()
