#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def order_endpoints(x1, x2, y1, y2):
    '''order the points so that (x1, y1) is on the left'''
    if x1 <= x2:
        return(x1, y1, x2, y2)
    else:
        return(x2, y2, x1, y1)

def main():
    s = get_input('input.txt')

    graph = defaultdict(lambda: defaultdict(int))
    total_intersections = 0

    for segment in s:
        endpoints = segment.split(' -> ')
        x1, y1 = map(int, endpoints[0].split(','))
        x2, y2 = map(int, endpoints[1].split(','))

        #edge case if slope is undefined
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(0, y2 - y1 + 1):
                graph[x1][y1 + y] += 1
                if graph[x1][y1 + y] == 2:
                    total_intersections += 1
            continue

        #otherwise, calculate slope as normal
        x1, y1, x2, y2 = order_endpoints(x1, x2, y1, y2)
        slope = (y2 - y1)//(x2 - x1)
        #skip if not horizontal, vertical done beforee
        while x1 != x2 or y1 != y2:
            graph[x1][y1] += 1
            if graph[x1][y1] == 2:
                total_intersections += 1
            x1 += 1
            y1 += slope
        #also get the last endpoint
        graph[x2][y2] += 1
        if graph[x2][y2] == 2:
            total_intersections += 1

    print(total_intersections)
    #print(graph)

main()

# < 14000
