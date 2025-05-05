#!/opt/anaconda3/envs/py39/bin/python
#Jake Feiler

import sys
import math

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')

    current_points = []

    turns = s[0]
    directions = {}
    for node in s[2:]:
        start, ends = node.split(' = (')
        end1,end2 = ends.split(', ')
        end2 = end2[:-1]
        directions[start] = tuple([end1, end2])
        if start[-1] == 'A':
            current_points.append(start)

    map_point = 0
    length_of_map = len(turns)

    closest_distances = [0] * len(current_points)

    while min(closest_distances) == 0:
        next_direction = turns[map_point%length_of_map]
        map_point += 1
        if next_direction == 'L':
            for pos, current_point in enumerate(current_points):
                new_point = directions[current_point][0]
                current_points[pos] = new_point
                if new_point[-1] == 'Z' and closest_distances[pos] == 0:
                    closest_distances[pos] = map_point
        else:
            for pos, current_point in enumerate(current_points):
                new_point = directions[current_point][1]
                current_points[pos] = new_point
                if new_point[-1] == 'Z' and closest_distances[pos] == 0:
                    closest_distances[pos] = map_point

    total_distance = 1

    #Not proper solution, but hope answer is lcm of closest distance to each

    total_distance = 1
    for distance in closest_distances:
        total_distance = math.lcm(total_distance, distance)

    print(total_distance)

main()
