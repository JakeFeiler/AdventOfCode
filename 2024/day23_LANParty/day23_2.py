#!/opt/anaconda3/bin/python
#Jake Feiler

import sys
from collections import defaultdict as dd

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    return [line.strip() for line in input_file]

def main():
    s = get_input('input.txt')
    #Create a dictionary to map all machines to their connected parts
    connections = dd(set)
    
    #Track sets of increasing size, starting with given pairs
    biggest_sets = set()
    for machine_pair in s:
        first, second = machine_pair.split('-')
        connections[first].add(second)
        connections[second].add(first)
        biggest_sets.add((first, second))

    #Iterate until down to one final set
    #Start with pairs, than trios, and so on...
    while len(biggest_sets) > 1:
        next_biggest_sets = set()
        for candidate in biggest_sets:
            links = connections[candidate[0]]
            #With the current set of size N, find all links shared by all members of the set
            for paired_node in candidate[1:]:
                links = links.intersection(connections[paired_node])
            #Create sets of size N + 1 with these new common links
            for additional_node in links:
                candidate = list(candidate)
                candidate.append(additional_node)
                candidate.sort()
                next_biggest_sets.add(tuple(candidate))
        biggest_sets = next_biggest_sets

    biggest_set = biggest_sets.pop()
    print(','.join(biggest_set))


main()
